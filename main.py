from personinfo import get_person_info
from addtask import add_task
from addtask import tasks
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
person_info = get_person_info(name, age, email)
add_task()
print(tasks)