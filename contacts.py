
f =  open("contacts.txt", "a")
contact_list = []

class Contacts:
	def __init__(self, name, phone_number, email, address):
		self.Name = name
		self.PhoneNumber = phone_number
		self.Email = email
		self.Address = address

	def relay_info(self):
		print_info = ("Name: {obj.Name} \n Phone number: {obj.PhoneNumber} \n Email: {obj.Email} \n Address: {obj.Address} \n".format(obj=self))
		return print_info

	def name(self):
		return contact_name

	def number(self):
		return self.PhoneNumber

	def email_address(self):
		return self.Email


def add_contact():
	new_contact = input("Enter new contact name.\n")
	new_number = input("Enter new contact's phone number.\n")
	new_email = input("Enter new contact's Email address (if none, enter 'n/a').\n")
	new_address = input("Enter new contact's address (if none, enter 'n/a').\n")

	new_contact = new_contact.title()
	new_contact = Contacts(new_contact, new_number, new_email, new_address)
	# new_contact.join(contact_list)
	contact_list.append(new_contact)
	# f.write()

def edit_contact():
	contact_edit = input("What is the name of the contact you would like to edit?\n")
	contact_edit = contact_edit.title()
	for _ in contact_list:
		if contact_edit == _.Name:

			field_edit = input("What field would you like to edit?\n").lower()
			if field_edit == "name":
				new_name = input("Enter a new name for this contact.\n")
				_.Name = new_name.title()
			elif field_edit == "number":
				new_number = input("Enter a new phone number for this contact.\n")
				_.Number = new_number
			elif field_edit == "email":
				new_email = input("Enter a new email address for this contact.\n")
				_.Email = new_email
			elif field_edit == "address":
				new_address = input("Enter a new address for this contact.\n")
				_.Address = new_address
			elif field_edit == "cancel":
				pass
		else:
			print("I don't know that contact.\n")

def list_contacts():
	for _ in contact_list:
		print(_.relay_info() + "\n---------------------\n")


def search_contacts():
	search = input("Enter contact name.\n")
	search = search.title()
	for _ in contact_list:
		if _.Name == search:
			print (_.relay_info())
		else:
			print("I don't know that contact.\n")


def remove_contact():
	remove = input("Which contact would you like to remove?\n")
	remove = remove.title()
	for _ in contact_list:
		if remove == _.Name:
			answer = input("Are you sure you want to remove this contact?")
			if answer.lower() == "yes":
				contact_list.remove(_)
			else:
				print("OK {obj.Name} can stay...for now.".format(obj=_))
		else:
			print("I don't knwo that contact.\n")

def main():
	running = True
	while running:
		selection = input("Would you like to add, remove, edit, search or list contacts?(remove currently unavailable)\n")
		selection = selection.lower()
		if selection == "add":
			add_contact()
		elif selection == "edit":
			edit_contact()
		elif selection == "search":
			search_contacts()
		elif selection == "list":
			list_contacts()
		elif selection == "remove":
			remove_contact()
		elif selection == "quit":
			running = False
		else:
			print("I don't know that contact.\n")

if __name__ == '__main__':
	main()