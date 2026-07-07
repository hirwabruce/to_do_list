from addtask import load_tasks, save_tasks, tasks
def update_status(task_name):
    for task in tasks:
        if task["name"] == task_name:
            task["status"] = "Completed"
            save_tasks()  # Save changes to data.txt
            print("Task completed successfully.")
            return

    print("Task not found.")