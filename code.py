tasks = []

def add_task():
    name = input("Enter task name: ")
    print("Urgency (1-low, 2-medium, 3-high):")
    urg = int(input())
    print("Importance (1-low, 2-medium, 3-high):")
    imp = int(input())
    print("Difficulty (1-easy, 2-medium, 3-hard):")
    diff = int(input())
    priority = urg + imp + diff
    task = {
        "name": name,
        "urgency": urg,
        "importance": imp,
        "difficulty": diff,
        "priority": priority
    }
    tasks.append(task)
def show_tasks():
    sorted_list = sorted(tasks, key=lambda x: x["priority"], reverse=True)
    print("\nPriority List:")
    for t in sorted_list:
        print(t["name"], "- Priority:", t["priority"])
while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid option")

