import tkinter as tk
from tkinter import ttk, messagebox
from optimizer import Task, greedy_selection, get_missed_tasks

# COLORS (same theme)
BG = "#1e1e2e"
PANEL = "#2a2a3d"
ACCENT = "#7c6af7"
SUCCESS = "#56cfad"
TEXT = "#e0e0f0"
TEXT_DIM = "#888aaa"
WHITE = "#ffffff"
CARD = "#33334a"


class OptiDayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OptiDay – Smart Task Optimizer")
        self.root.geometry("1000x700")
        self.root.configure(bg=BG)

        self.tasks = []
        self.build_ui()

    def build_ui(self):
        # HEADER
        header = tk.Frame(self.root, bg=ACCENT)
        header.pack(fill="x")

        tk.Label(header, text="⚡ OptiDay – Smart Task Optimizer",
                 font=("Helvetica", 18, "bold"),
                 fg=WHITE, bg=ACCENT).pack(pady=10)

        # MAIN BODY
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=15, pady=10)

        # LEFT PANEL
        left = tk.Frame(body, bg=PANEL, padx=10, pady=10)
        left.pack(side="left", fill="y")

        # INPUTS
        self.entry_name = self.create_entry(left, "Task Name")
        self.entry_duration = self.create_entry(left, "Duration")
        self.entry_priority = self.create_entry(left, "Priority")
        self.entry_deadline = self.create_entry(left, "Deadline")

        tk.Button(left, text="Add Task", bg=ACCENT, fg=WHITE,
                  command=self.add_task).pack(fill="x", pady=5)

        self.entry_total = self.create_entry(left, "Total Time")

        tk.Button(left, text="Optimize", bg=SUCCESS, fg=BG,
                  command=self.optimize).pack(fill="x", pady=10)

        # TASK LIST
        self.listbox = tk.Listbox(left, bg=CARD, fg=TEXT, height=10)
        self.listbox.pack(fill="both", expand=True)

        # RIGHT PANEL (RESULT)
        self.right = tk.Frame(body, bg=BG)
        self.right.pack(side="right", fill="both", expand=True)

        tk.Label(self.right, text="Results will appear here",
                 fg=TEXT_DIM, bg=BG).pack(pady=20)

    def create_entry(self, parent, label):
        tk.Label(parent, text=label, fg=TEXT_DIM, bg=PANEL).pack(anchor="w")
        entry = tk.Entry(parent, bg=CARD, fg=TEXT)
        entry.pack(fill="x", pady=5)
        return entry

    def add_task(self):
        try:
            name = self.entry_name.get()
            duration = int(self.entry_duration.get())
            priority = int(self.entry_priority.get())
            deadline = int(self.entry_deadline.get())

            task = Task(name, duration, priority, deadline)
            self.tasks.append(task)

            self.listbox.insert(tk.END, f"{name} | {duration}h | P:{priority}")

            # clear fields
            self.entry_name.delete(0, tk.END)
            self.entry_duration.delete(0, tk.END)
            self.entry_priority.delete(0, tk.END)
            self.entry_deadline.delete(0, tk.END)

        except:
            messagebox.showerror("Error", "Enter valid values")

    def optimize(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "Add tasks first")
            return

        try:
            total_time = int(self.entry_total.get())
        except:
            messagebox.showerror("Error", "Enter valid total time")
            return

        selected, score, time_used = greedy_selection(self.tasks, total_time)
        missed = get_missed_tasks(self.tasks, selected)

        # CLEAR RIGHT PANEL
        for widget in self.right.winfo_children():
            widget.destroy()

        # RESULT HEADER
        tk.Label(self.right, text="Optimized Schedule",
                 font=("Helvetica", 14, "bold"),
                 fg=ACCENT, bg=BG).pack(pady=10)

        # SCORE
        tk.Label(self.right, text=f"Score: {score}",
                 fg=SUCCESS, bg=BG, font=("Helvetica", 12)).pack()

        tk.Label(self.right, text=f"Time Used: {time_used}",
                 fg=TEXT, bg=BG).pack()

        # SELECTED TASKS
        tk.Label(self.right, text="\n✅ Selected Tasks",
                 fg=SUCCESS, bg=BG).pack()

        for t in selected:
            tk.Label(self.right, text=t.name, fg=TEXT, bg=BG).pack()

        # MISSED TASKS
        tk.Label(self.right, text="\n❌ Missed Tasks",
                 fg="red", bg=BG).pack()

        for t in missed:
            tk.Label(self.right, text=t.name, fg=TEXT, bg=BG).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = OptiDayApp(root)
    root.mainloop()