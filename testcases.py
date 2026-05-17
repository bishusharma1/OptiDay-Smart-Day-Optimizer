from optimizer import Task, greedy_selection

def run_tests():
    print("Running Greedy Tests...\n")

    tasks = [
        Task("Study", 2, 50, 4),
        Task("Workout", 3, 60, 6),
        Task("Project", 3, 70, 5),
    ]

    total_time = 5

    selected, score, time = greedy_selection(tasks, total_time)

    print("Selected Tasks:")
    for t in selected:
        print(t.name)

    print("\nScore:", score)
    print("Time Used:", time)


if __name__ == "__main__":
    run_tests()