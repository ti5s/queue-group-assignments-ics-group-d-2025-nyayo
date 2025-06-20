import threading

class PrintQueueManager:
    def __init__(self, capacity=10, expiry_time=10, aging_interval=5):
        self.capacity = capacity
        self.queue = []
        self.lock = threading.Lock()
        self.current_time = 0
        self.expiry_time = expiry_time
        self.aging_interval = aging_interval

    def enqueue_job(self, user_id, job_id, priority):
        with self.lock:
            if len(self.queue) >= self.capacity:
                print("Queue full.")
                return
            self.queue.append({
                "user_id": user_id,
                "job_id": job_id,
                "priority": priority,
                "waiting_time": 0,
                "timestamp": self.current_time
            })

    def apply_priority_aging(self):
        for job in self.queue:
            if job["waiting_time"] > 0 and job["waiting_time"] % self.aging_interval == 0:
                job["priority"] += 1
        self.queue.sort(key=lambda x: (-x["priority"], x["waiting_time"]))

    def remove_expired_jobs(self):
        original_len = len(self.queue)
        self.queue = [
            job for job in self.queue
            if (self.current_time - job["timestamp"]) <= self.expiry_time
        ]
        if len(self.queue) != original_len:
            print("Expired jobs removed.")

    def handle_simultaneous_submissions(self, jobs):
        threads = []
        for job in jobs:
            t = threading.Thread(target=self.enqueue_job, args=(job["user_id"], job["job_id"], job["priority"]))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

    def tick(self):
        self.current_time += 1
        for job in self.queue:
            job["waiting_time"] += 1
        self.apply_priority_aging()
        self.remove_expired_jobs()

    def print_job(self):
        with self.lock:
            if self.queue:
                job = self.queue.pop(0)
                print(f"Printed Job: {job}")
            else:
                print("No jobs to print.")

    def show_status(self):
        print(f"Time: {self.current_time}")
        print("Queue Snapshot:")
        for job in self.queue:
            print(f"JobID: {job['job_id']} | User: {job['user_id']} | Priority: {job['priority']} | Waiting: {job['waiting_time']}")
