import tkinter as tk
from tkinter import messagebox
import time

 # Backend logic for the print queue
class CircularPrinterQueue:
    CAPACITY = 10

    def __init__(self):
        self.data = [[None, None, None, None]] * self.CAPACITY
        self.front = 0
        self.size = 0
        self.jobId = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.CAPACITY

    def enqueue(self, user_id):
        if self.is_full():
            return "❌ The queue is full!"
        avail = (self.size + self.front) % self.CAPACITY
        self.jobId += 1
        job_id = self.jobId
        priority = 1
        waiting_time = time.perf_counter_ns()
        self.data[avail] = [user_id, job_id, priority, waiting_time]
        self.size += 1
        return f"✅ Job {job_id} submitted by user {user_id}."

    def dequeue(self):
        if self.is_empty():
            return "❌ Queue is empty. No job to print."
        output = self.data[self.front]
        self.data[self.front] = [None, None, None, None]
        self.front = (self.front + 1) % self.CAPACITY
        self.size -= 1
        return f"🖨️ Printed Job {output[1]} submitted by {output[0]}."

    def show_status(self):
        return [job for job in self.data if job[0] is not None]


# GUI front-end using Tkinter
class PrinterQueueApp:
    def __init__(self, master):
        self.queue = CircularPrinterQueue()
        self.master = master
        master.title("🖨️ Printer Queue Simulator")

        self.label = tk.Label(master, text="Enter User ID:")
        self.label.pack()

        self.user_entry = tk.Entry(master)
        self.user_entry.pack()

        self.add_button = tk.Button(master, text="Submit Print Job", command=self.enqueue_job)
        self.add_button.pack()

        self.print_button = tk.Button(master, text="Print Next Job", command=self.dequeue_job)
        self.print_button.pack()

        self.status_button = tk.Button(master, text="Show Queue Status", command=self.show_queue)
        self.status_button.pack()

        self.output_text = tk.Text(master, height=15, width=60)
        self.output_text.pack()

    def enqueue_job(self):
        user_id = self.user_entry.get()
        if user_id:
            msg = self.queue.enqueue(user_id)
            self.output_text.insert(tk.END, msg + "\n")
            self.user_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "⚠️ Please enter a User ID.")

    def dequeue_job(self):
        msg = self.queue.dequeue()
        self.output_text.insert(tk.END, msg + "\n")

    def show_queue(self):
        self.output_text.insert(tk.END, "\n--- 📋 Current Queue ---\n")
        for job in self.queue.show_status():
            self.output_text.insert(tk.END, f"User: {job[0]}, Job ID: {job[1]}, Priority: {job[2]}\n")


# Start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = PrinterQueueApp(root)
    root.mainloop()
