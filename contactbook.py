class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts in the contact book.")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            print("Search Results:")
            for i, contact in enumerate(found_contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No matching contacts found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
            print("Contact added successfully!")
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
