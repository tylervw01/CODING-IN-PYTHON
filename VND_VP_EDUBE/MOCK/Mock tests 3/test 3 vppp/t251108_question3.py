#Question 3

def display_menu(): # DISPLAY MENU FUNCTION
    print("\nContact List Manager") # PRINT
    print("1. Add Contact") # PRINT
    print("2. Delete Contact") # PRINT
    print("3. List Contacts") # PRINT
    print("4. Exit") # PRINT
    
def add_contact(contacts): # ADD CONTACT
    name = input("Enter contact name: ") # INPUT
    phone = input("Enter contact phone number: ") # INPUT
    contacts[name] = phone # DICYIONARY
    print("Contact added successfully!") # PRINT
    
def delete_contact(contacts): # DELETE CONTACT
    name = input("Enter contact name to delete: ") # INPUT
    
    if name in contacts: # IF STATEMENT
        del contacts[name] # DELETE
        print("Contact deleted successfully!") # PRINT
    else: # ELSE
        print("Contact not found.") # PRINT

def list_contacts(contacts): # LIST CONTACT
    print("Contact List:") # PRINT

    for name, phone in contacts.items(): # FOR LOOP
        print(f"{name}: {phone}") # PRINT
contacts = {} # DICTIONARY TO STORE CONTACTS

while True: # WHILE LOOP

    display_menu() # DISPALY MENU
    choice = input("Enter your choice: ") # INPUT
    if choice == "1": # IF STATEMENT
        add_contact(contacts) # ADD CONTACT
    elif choice == "2": # ELSE IF STATEMENT
        delete_contact(contacts) # DELETE CONTACT
    elif choice == "3": # ELSE IF STATEMENT
        list_contacts(contacts) # LIST CONTACT
    elif choice == "4": # ELSE IF STATEMENT
        print("Exiting program.") # PRINT
        break # BREAK
    else: # ELSE
        print("Invalid choice. Please try again.") # PRINT
        continue # CONTINUE

    input("Press Enter to continue...") # INPUT

    print("Exiting program.") # PRINT
    break # BREAK