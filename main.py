from personinfo import get_person_info

name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
person_info = get_person_info(name, age, email)
print("Person Information:")
print(f"Name: {person_info['name']}")
print(f"Age: {person_info['age']}")
print(f"Email: {person_info['email']}")