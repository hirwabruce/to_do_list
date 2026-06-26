from addtask import tasks

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
        