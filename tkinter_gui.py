import tkinter as tk
from tkinter import ttk
from print_queue_manager import PrintQueueManager

class QueueGUI:
    def __init__(self, root):
        self.manager = PrintQueueManager()
        self.root = root
        self.root.title("Print Queue Simulator")

        # Input Frame
        self.input_frame = ttk.LabelFrame(root, text="Add Print Job")
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self.input_frame, text="User ID:").grid(row=0, column=0)
        self.user_id_entry = ttk.Entry(self.input_frame)
        self.user_id_entry.grid(row=0, column=1)

        ttk.Label(self.input_frame, text="Job ID:").grid(row=1, column=0)
        self.job_id_entry = ttk.Entry(self.input_frame)
        self.job_id_entry.grid(row=1, column=1)

        ttk.Label(self.input_frame, text="Priority:").grid(row=2, column=0)
        self.priority_entry = ttk.Entry(self.input_frame)
        self.priority_entry.grid(row=2, column=1)

        self.add_button = ttk.Button(self.input_frame, text="Add Job", command=self.add_job)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Control Buttons
        self.control_frame = ttk.Frame(root)
        self.control_frame.grid(row=1, column=0, pady=10)

        self.tick_button = ttk.Button(self.control_frame, text="Tick", command=self.tick)
        self.tick_button.grid(row=0, column=0, padx=5)

        self.print_button = ttk.Button(self.control_frame, text="Print Job", command=self.print_job)
        self.print_button.grid(row=0, column=1, padx=5)

        self.refresh_button = ttk.Button(self.control_frame, text="Refresh Status", command=self.show_status)
        self.refresh_button.grid(row=0, column=2, padx=5)

        # Queue Status
        self.status_frame = ttk.LabelFrame(root, text="Queue Status")
        self.status_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.status_text = tk.Text(self.status_frame, height=15, width=60)
        self.status_text.pack()

        self.show_status()

    def add_job(self):
        user_id = self.user_id_entry.get()
        job_id = self.job_id_entry.get()
        try:
            priority = int(self.priority_entry.get())
        except ValueError:
            priority = 1
        self.manager.enqueue_job(user_id, job_id, priority)
        self.show_status()

    def tick(self):
        self.manager.tick()
        self.show_status()

    def print_job(self):
        self.manager.print_job()
        self.show_status()

    def show_status(self):
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, f"Time: {self.manager.current_time}\n")
        self.status_text.insert(tk.END, "Queue Snapshot:\n")
        for job in self.manager.queue:
            line = f"JobID: {job['job_id']} | User: {job['user_id']} | Priority: {job['priority']} | Waiting: {job['waiting_time']}\n"
            self.status_text.insert(tk.END, line)

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueGUI(root)
    root.mainloop()
