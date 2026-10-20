from Handle_error import InvalidPhoneError , ContactNotFoundError
class Contact:
    def __init__(self, name , contact_ID):
        self.name= name
        self.contact_ID= contact_ID
        self.__phone =None
    def get_phone(self):
        return self.__phone
    def set_phone(self, new_phone):
        if isinstance(new_phone, int):
            new_phone= str(new_phone)
        if not (isinstance(new_phone, str) and new_phone.isdigit() and 8 <= len(new_phone) <= 10):
            raise InvalidPhoneError ("Invalid Phone Number! It must contain only digits and be between 8 and 10 characters long.")
        self.__phone = new_phone
    def get_contact_type(self):
        return "General"
    def display_info(self):
        print("="*25)
        print(f"Name: {self.name}")
        print(f"Type: {self.get_contact_type()}")
        print(f"Phone: {self.get_phone()}")
class FamilyContact(Contact):
    def __init__(self, name, contact_ID, relationship, birthday):
        super().__init__(name ,contact_ID)
        self.relationship= relationship
        self.birthday= birthday
    def display_info(self):
        super().display_info()
        print(f"Relationship: {self.relationship}")
        print(f"Birthday: {self.birthday}")
        print("="*25)
    def get_contact_type(self):
        return "Family"
class WorkContact(Contact):
    def __init__(self, name , contact_ID , company , job_title):
        super().__init__(name, contact_ID)
        self.company = company
        self.job_title = job_title
    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")
        print(f"Job Title: {self.job_title}")
    def get_contact_type(self):
        return "Work"
class ContactBook:
    def __init__(self):
        self.contacts= {}  #contacts stored by contact_ID
    def add_contact(self,contact):
        if not isinstance(contact , Contact):
            raise TypeError("Contact must be a contact object")
        if not contact.contact_ID or not contact.contact_ID.strip():
            raise ValueError("Contact ID cannot be empty")
        if contact.contact_ID in self.contacts:
            raise ValueError(f"Contact ID {contact.contact_ID} already exits")
        self.contacts[contact.contact_ID]=contact
    def find_contact(self, contact_ID):
        if contact_ID not in self.contacts:
            raise ContactNotFoundError(f"Contact ID {contact_ID} not found")
        return self.contacts.get(contact_ID)
    def remove_contact(self , contact_ID):
        if contact_ID not in self.contacts:
            raise ContactNotFoundError(f"Contact ID {contact_ID} not found")
        return self.contacts.pop(contact_ID,None)
    def update_phone(self,contact_ID, new_phone):
        try:
            contact = self.find_contact(contact_ID)
            contact.set_phone(new_phone)
        except ContactNotFoundError as error:
            print(error)
            return False
        except InvalidPhoneError as error :
            print(error)
            return False
        return True
    def show_all_contacts(self):
        if not self.contacts:
            print("No contacts to show.")
            return
        for contact in sorted(self.contacts.values(),key=lambda contact: contact.name.casefold()):
            contact.display_info()
    def search_by_name(self,name ):
        search_name = name.strip().casefold()
        matches = [contact for contact in self.contacts.values() 
                if search_name in contact.name.casefold()
                ]
        if not matches:
            print(f"No contact found with name: {name}")
            return []
        for contact in matches:
            contact.display_info()
        return matches
    def get_contacts_by_type(self,contact_type):
        print(f"[{contact_type} Contact]")
        findcontact= [contact for contact in self.contacts.values()
                    if contact.get_contact_type().casefold() == contact_type.casefold() 
                    ]
        if not findcontact:
            print(f"No {contact_type} contacts found.")
            return []
        for contact in findcontact:
            contact.display_info()
        return findcontact
    def count_contact(self):
        return len(self.contacts)
book= ContactBook()
general = Contact("Lychhun", "C100")
general.set_phone("092996962")
book.add_contact(general)
while True:
    print("="*8, "Contact Book Menu", "="*8)
    print("1.Add General contact")
    print("2.Add family contact")
    print("3.Add work contact")
    print("4.Update phone number")
    print("5.Search by name")
    print("6.Show all contact")
    print("7.Show contact by type")
    print("8.Remove contact")
    print("9.Show total contacts")
    print("10.Exit")
    print("="*28)
    while True:
        choice= input("Enter your choice in our program: ").strip()
        if choice in {"1", "2", "3", "4", "5", "6", "7", "8", "9","10"}:
            break
        print("Please choice 1-10 options we don't have more option")
    if choice == "10":
        break
    match choice:
        case "1":
            name = input("Enter name: ")
            contact_ID = input("Enter contact ID: ")
            general = Contact(name, contact_ID)
            while True:
                try:
                    phone= input("Enter phone number: ")
                    general.set_phone(phone)
                    break
                except InvalidPhoneError as error:
                    print(error)
            try:
                book.add_contact(general)
                print("General contact added.")
            except ValueError as error:
                print(error)
        case "2":
            name= input("Enter name: ")
            contact_ID= input("Enter contact ID: ")
            relationship= input("Enter relationship: ")
            birthday= input("Enter birthday: ")
            family = FamilyContact(name, contact_ID, relationship, birthday)
            while True:
                try:
                    phone= input("Enter phone number: ")
                    family.set_phone(phone)
                    break
                except InvalidPhoneError as error:
                    print(error)
            try:
                book.add_contact(family)
                print("Family contact added.")
            except ValueError as error:
                print(error)
        case "3":
            name= input("Enter name: ")
            contact_ID= input("Enter contact ID: ")
            company= input("Enter company name: ")
            job_title= input("Enter job title: ")
            work= WorkContact(name, contact_ID, company, job_title)
            while True:
                try:
                    phone = input("Enter phone number: ")
                    work.set_phone(phone)
                    break
                except InvalidPhoneError as error:
                    print(error)
            try:
                book.add_contact(work)
                print("Work contact added.")
            except ValueError as error:
                print(error)
        case "4":
            contact_ID = input("Enter contact ID: ")
            new_phone = input("Enter new phone number: ")
            if book.update_phone(contact_ID, new_phone):
                print("Phone number updated.")
        case "5":
            search_by_name = input("Enter name that you search: ").strip()
            if not search_by_name:
                print("Please enter a name.")
            else:
                book.search_by_name(search_by_name)
        case "6":
            book.show_all_contacts()
        case "7":
            contact_type = input("Enter type (Family, Work, General): ").strip()
            book.get_contacts_by_type(contact_type)
        case "8":
            remove_ID_contact= input("Enter contact ID to remove: ")
            try:
                remove = book.remove_contact(remove_ID_contact)
                print(f"Removed {remove.name}.")
            except ContactNotFoundError as error:
                print(error)
        case "9":
            print(f"Total contacts: {book.count_contact()}")