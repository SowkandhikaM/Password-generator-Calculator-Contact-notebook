contacts = []

def add_contact():
    print("\nAdd Contact")
    name = input(" Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully")

def view_contacts():
    print("\nContact List")
    if not contacts:
        print("No contacts available")
    else:
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. {c['name']} – {c['phone']}")

def search_contact():
    print("\nSearch Contact")
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c['name'].lower() or keyword in c['phone']:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    print("\nUpdate Contact")
    name = input("Enter the name to update: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["phone"] = input("New Phone Number: ")
            c["email"] = input("New Email: ")
            c["address"] = input("New Address: ")
            print("Contact updated successfully")
            return
    print("Contact not found.")

def delete_contact():
    print("\nDelete Contact")
    name = input("Enter the name to delete: ")
    for i, c in enumerate(contacts):
        if c["name"].lower() == name.lower():
            del contacts[i]
            print("Contact deleted successfully")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Management")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1‑6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

if _name_ == "_main_":
    main()
