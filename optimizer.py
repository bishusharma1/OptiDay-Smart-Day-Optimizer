class Task:
    def __init__(self, name, duration, priority, deadline):
        self.name = name
        self.duration = duration
        self.priority = priority
        self.deadline = deadline


def greedy_selection(tasks, total_time):
    # Sort by priority (desc) and deadline (asc)
    tasks_sorted = sorted(tasks, key=lambda t: (-t.priority, t.deadline))

    selected = []
    time_used = 0
    total_score = 0

    for task in tasks_sorted:
        if time_used + task.duration <= total_time:
            selected.append(task)
            time_used += task.duration
            total_score += task.priority

    return selected, total_score, time_used


def get_missed_tasks(all_tasks, selected_tasks):
    selected_names = {t.name for t in selected_tasks}
    return [t for t in all_tasks if t.name not in selected_names]