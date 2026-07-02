from personinfo import get_person_info,person_info, save_person_info, load_person_info,view_person_info
from addtask import add_task, load_tasks, save_tasks,get_valid_date
from addtask import tasks
from viewtasks import view_tasks

load_tasks()
person_info = load_person_info()        
if not person_info:
    print("Please enter your personal information.")
    name = input("Enter your name: ")
    dob = get_valid_date("Enter your date of birth (YYYY-MM-DD): ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    person_info = get_person_info(name, dob, email, address, phone)
    save_person_info(person_info)
print("Welcome to the To-Do List Application!")
print("Menu:")
print("1. Tasks")
print("2. Profile")
print("3. Exit")
choice_1=input("Enter your choice(1-3): ")
if choice_1=='2':
    
    print("Welcome to your profile")
    print("1.Edit the profile")
    print("2.View the profie")
    choice_2=input("Type'edit'or'1' to edit the profile and 'view'or '2' to view the profile. ")
    if choice_2.lower=='2' or choice_2.lower=='view':
        view_person_info(person_info)
    
#add_task()
#save_tasks()
#view_tasks()
