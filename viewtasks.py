from addtask import tasks
from datetime import date

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"Task {index}:")
        print(f"  Name: {task['name']}")
        print(f"  Description: {task['description']}")
        print(f"  Date Created: {task['date_created']}")
        print(f"  Due Date: {task['due_date']}")
        print(f"  Status: {task['status']}")
        print("-" * 20)

def view_tasks_due_today():
    today = date.today().isoformat()
    tasks_due_today = [task for task in tasks if task["due_date"] == today]

    if not tasks_due_today:
        print("No tasks due today.")
        return

    print(f"Tasks due today ({today}):")
    for index, task in enumerate(tasks_due_today, start=1):
        print(f"Task {index}:")
        print(f"  Name: {task['name']}")
        print(f"  Description: {task['description']}")
        print(f"  Date Created: {task['date_created']}")
        print(f"  Due Date: {task['due_date']}")
        print(f"  Status: {task['status']}")
        print("-" * 20)
