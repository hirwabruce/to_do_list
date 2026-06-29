person_info = {}
def get_person_info(name, dob, email, address, phone):
    person_info = {
        "name": name,
        "dob": dob,
        "email": email,
        "address": address,
        "phone": phone
    }
    return person_info
def save_person_info(person_info):
    with open("personinfo.txt", "w") as file:
        file.write(f"{person_info['name']},{person_info['dob']},{person_info['email']},{person_info['address']},{person_info['phone']}\n")
def load_person_info():
    try:
        with open("personinfo.txt", "r") as file:
            line = file.readline().strip()
            if line:
                name, dob, email, address, phone = line.split(",")
                return {
                    "name": name,
                    "dob": dob,
                    "email": email,
                    "address": address,
                    "phone": phone
                }
    except FileNotFoundError:
        return None
    
def view_person_info(person_info):
    print("Personal Information:")
    print(f"  Name: {person_info['name']}")
    print(f"  Date of Birth: {person_info['dob']}")
    print(f"  Email: {person_info['email']}")
    print(f"  Address: {person_info['address']}")
    print(f"  Phone: {person_info['phone']}")    