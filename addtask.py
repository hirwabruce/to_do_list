from datetime import date, datetime


tasks=[]
def get_valid_date(prompt):
    while True:
        user_date = input(prompt)

        try:
            # Validate format and date
            datetime.strptime(user_date, "%Y-%m-%d")
            return user_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def add_task():
    while True:
        task_name=input("Enter the task name (or type 'exit' to finish): ")
        if task_name.lower() == 'exit':
            break
        task_description=input("Enter the task description: ")
        date_created=date.today().isoformat()
        task_due_date=get_valid_date("Enter the task due date (YYYY-MM-DD): ")
        task_status="Pending"
        today = datetime.now().strftime("%Y%m%d")

        # Count tasks created today
        count = sum(task["id"].startswith(today) for task in tasks) + 1

        task_id = f"{today}-{count}"

        task=dict()
        task["id"]=task_id
        task["name"]=task_name
        task["description"]=task_description
        task["date_created"]=date_created   
        task["due_date"]=task_due_date
        task["status"]=task_status
        tasks.append(task)

def save_tasks():

    with open("data.txt", "w") as file:

        for task in tasks:

         file.write(
    f"{task['id']},{task['name']},{task['description']},{task['date_created']},{task['due_date']},{task['status']}\n"
)

def load_tasks():
    tasks.clear()
    try:

        with open("data.txt", "r") as file:

            for line in file:

                task_id, name, description, date_created, due_date, status = line.strip().split(",")

                tasks.append({
                    "id": task_id,
                    "name": name,
                    "description": description,
                    "date_created": date_created,
                    "due_date": due_date,
                    "status": status
                })

    except FileNotFoundError:
        pass         