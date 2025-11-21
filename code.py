tasks = []

def add_task():
    name = input("Task name: ")

    print("Rate urgency (1=low, 2=medium, 3=high): ")
    urgency = int(input("> "))

    print("Rate importance (1=low, 2=medium, 3=high): ")
    importance = int(input("> "))

    print("Rate difficulty (1=easy, 2=medium, 3=hard): ")
    difficulty = int(input("> "))

    priority = urgency + importance + difficulty

    tasks.append({
        "name": name,
        "urgency": urgency,
        "importance": importance,
        "difficulty": difficulty,
        "priority": priority
    })

def show_tasks():
    sorted_tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)
    print("\n--- PRIORITY LIST ---")
    for t in sorted_tasks:
        print(f"{t['name']}  -> Priority: {t['priority']}")

while True:
    print("\n1. Add Task")
    print("2. Show Priority List")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
