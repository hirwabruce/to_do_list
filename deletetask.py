"""from addtask import tasks, save_tasks, load_tasks

def delete_task(task_name,):
    for task in tasks:
        if task["name"].lower() == task_name.lower():
            tasks.remove(task)
            save_tasks()
            print(f"Task '{task_name}' deleted successfully.")
            return

    print(f"Task '{task_name}' not found.")""" 
from addtask import load_tasks, save_tasks, tasks
def delete_task_status(task_name):
    for task in tasks:
        if task["name"] == task_name:
            task["status"] = "Deleted"
            save_tasks()  # Save changes to data.txt
            print("Task deleted successfully.")
            return

    print("Task not found.")