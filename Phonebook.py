
#declare variables
Name= ""
email=""
option= ""




# dictionary for storing contacts
contacts = {}

# This function will search for an email address by name
def lookup_email():
    name = input("Enter name to search: ")
    if name in contacts:
        email = contacts[name]
        print(f"Email address for {name}: {email}")
    else:
        print(f"{name} is not in your contacts.")

# This function will add a new name and an email address
def add_contact():
    name = input("Enter name to add: ")
    email = input("Enter email address: ")
    contacts[name] = email
    print(f"{name} mailto: {email} added to contacts with email address:")

# This function will edit an email address
def change_email():
    name = input("Enter the name to change email address: ")
    if name in contacts:
        email = input("Enter the new email address: ")
        contacts[name] = email
        print(f"Email address for {name} updated to: {email}")
    else:
        print(f"{name} not found in the contacts.")

# This function will delete an existing contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} and email has been deleted")
    else:
        print(f"{name} not found in the contacts.")

while True:
    print("\nMenu:")
    print("1. Search email address")
    print("2. Add new contact")
    print("3. Edit email address")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("Please select option (1/2/3/4/5): ")

    if choice == '1':
        lookup_email()
    elif choice == '2':
        add_contact()
    elif choice == '3':
        change_email()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Have a nice day.")
        break
    else:
        print("Invalid option. Please choose from (1/2/3/4/5).")


