contacts = {}

while True:
    print("\n------ Address Book ------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name : ").lower()
        if name in contacts:
            print("Contact already exixts")
        else :
            num = input("Enter your Number : ")
            contacts[name] = num
            print(f"Contact{name} added sucessfully")

    elif choice == '2':
        name = input("Enter the name of the contact : ").lower()
        if name in contacts:
            print(f"{name}'s contact number is {num}")
        else :
            print(f"Contact{name} not found")

    elif choice == '3':
        name = input("Enter the contact name you want to delete :")
        if name in contacts:
            del contacts[name]
            print(f"Contact deleted sucessfully")
        else:
            print(f"Contact not found ")
    elif choice == '4':
        name = input("Enter your contact name to update : ").lower()
        if name in contacts:
            num = input("Enter the updated number : ")
            contacts[name] = num
            print(f"Contact updated sucessfully")
        else :
            print("Contact not found ")
        
    elif choice == '5':
        if contacts:
            print("\nAll Contacts:")
            for name, number in contacts.items():
                print(f"{name} : {number}")
        else:
            print("No contacts found.")

    elif choice == '6':
        print("Exiting Address Book. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")