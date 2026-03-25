# Smart Gym Membership System Prototype
users = {"user@nci.ie": "password123"}
classes = {"1": {"name": "Yoga", "time": "10:00 AM", "capacity": 2},
           "2": {"name": "Spinning", "time": "12:00 PM", "capacity": 15}}
bookings = []

def login():
    print("--- Gym Login ---")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    if email in users and users[email] == password:
        print("Login Successful!\n")
        return email
    print("Invalid Credentials.")
    return None

def book_class(user):
    print("--- Available Classes ---")
    for cid, info in classes.items():
        print(f"ID: {cid} | {info['name']} at {info['time']} (Spots: {info['capacity']})")
    
    choice = input("\nEnter Class ID to book: ")
    if choice in classes and classes[choice]['capacity'] > 0:
        classes[choice]['capacity'] -= 1
        bookings.append({"user": user, "class": classes[choice]['name']})
        print(f"Successfully booked {classes[choice]['name']}!")
    else:
        print("Class full or invalid ID.")

# Main Program Flow
current_user = login()
if current_user:
    book_class(current_user)