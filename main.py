from print_queue_manager import PrintQueueManager

pq = PrintQueueManager()

# Simulated job events
pq.enqueue_job("user1", "job1", 1)
pq.tick()
pq.enqueue_job("user2", "job2", 2)
pq.tick()
pq.handle_simultaneous_submissions([
    {"user_id": "u3", "job_id": "j3", "priority": 1},
    {"user_id": "u4", "job_id": "j4", "priority": 3}
])
pq.tick()
pq.show_status()
pq.print_job()
