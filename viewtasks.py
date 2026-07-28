from addtask import tasks
from datetime import date

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
     
    for index, task in enumerate(tasks, start=1):
        if task["status"] == "Pending" or task["status"] == "Completed":
            print(f"Task {index}:")
            print(f"  Name: {task['name']}")
            print(f"  Description: {task['description']}")
            print(f"  Date Created: {task['date_created']}")
            print(f"  Due Date: {task['due_date']}")
            print(f"  Status: {task['status']}")
            print("-" * 20)

def view_tasks_due_today():
    today = date.today().isoformat()
    
    tasks_due_today = [task for task in tasks if task["due_date"] == today and task["status"] == "Pending"]
    
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

def percentage_tasks():
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks available.")
        return
    pending_tasks = sum(1 for task in tasks if task["status"] == "Pending")
    completed_tasks = sum(1 for task in tasks if task["status"] == "Completed")
    pending_percentage = (pending_tasks / total_tasks) * 100
    completed_percentage = (completed_tasks / total_tasks) * 100
    print(f"Percentage of pending tasks: {pending_percentage:.2f}%")
    print(f"Percentage of completed tasks: {completed_percentage:.2f}%")
