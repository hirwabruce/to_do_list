tasks=[]
def add_task():
    while True:
        task_name=input("Enter the task name (or type 'exit' to finish): ")
        if task_name.lower() == 'exit':
            break
        task_description=input("Enter the task description: ")
        date_created=input("Enter the task creation date (YYYY-MM-DD): ")
        task_due_date=input("Enter the task due date (YYYY-MM-DD): ")
        task_status="Pending"

        task=dict()
        task["name"]=task_name
        task["description"]=task_description
        task["date_created"]=date_created   
        task["due_date"]=task_due_date
        task["status"]=task_status
        tasks.append(task)

