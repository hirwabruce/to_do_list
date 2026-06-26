from personinfo import get_person_info
from addtask import add_task, load_tasks, save_tasks
from addtask import tasks
from viewtasks import view_tasks

load_tasks()
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
person_info = get_person_info(name, age, email)
add_task()
save_tasks()
view_tasks()
print(tasks)