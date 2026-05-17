from optimizer import Task, greedy_selection, get_missed_tasks

def print_tasks(tasks):
    for t in tasks:
        print(f"{t.name} | Time: {t.duration} | Priority: {t.priority}")

def main():
    print("OptiDay – Greedy Task Optimizer\n")

    tasks = []
    n = int(input("Enter number of tasks: "))
    total_time = int(input("Enter total available time: "))

    for i in range(n):
        print(f"\nTask {i+1}")
        name = input("Name: ")
        duration = int(input("Duration: "))
        priority = int(input("Priority: "))
        deadline = int(input("Deadline: "))

        tasks.append(Task(name, duration, priority, deadline))

    selected, score, time_used = greedy_selection(tasks, total_time)
    missed = get_missed_tasks(tasks, selected)

    print("\n--- Selected Tasks ---")
    print_tasks(selected)

    print("\n--- Missed Tasks ---")
    print_tasks(missed)

    utilization = (time_used / total_time) * 100

    print("\n📊 Summary")
    print("Productivity Score:", score)
    print("Time Used:", time_used)
    print("Utilization: {:.2f}%".format(utilization))


if __name__ == "__main__":
    main()