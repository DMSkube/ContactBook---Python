def main():
	contacts = open("contacts.txt", "r") # Opens/creates .txt
	contactsList = [] # Super-list
	line = contacts.readline() # Save first line of .txt as variable
	line = line.strip()	# Strip of spaces, save to itself
	while line != "": # Terminates loop when end of .txt is reached
		contact = [] # Sub-list
		for i in range(4):
			line = line.strip("\n")
			contact.append(line) # Append line to sub-list
			line = contacts.readline() #Open next line of .txt
		contactsList.append(contact) # Append sub-list to super-list
	contacts.close()

	menu(contactsList) # Call menu, pass along super-list

# Menu
def menu(contactsList):
	contactsList = contactsList
	repeat = True # Begin menu loop, ended by exitProgram()
	while repeat == True:
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print("Welcome to your contact book. Would you like to: \n")
		print("1. Add New Contact")
		print("2. Display All Contacts")
		print("3. Search For Contact")
		print("4. Edit Contact")
		print("5. Delete Contact")
		print("6. Exit\n")

		# Input Validation
		while True: 
			try:
				menuChoice = int(input("Enter your choice here: "))
			except ValueError: # Asks for new menuChoice if input is not an integer
				print("Error: Please enter a number from 1 to 6.")
				continue
			if menuChoice < 1 or menuChoice > 6: # Asks for new input if input is not a menu option
				print("Error: Please enter a number from 1 to 6.")
				continue
			else: # If input is validation, input is accepted
				break
		
		# Assess which option user chose with valid input

		# Add
		if menuChoice == 1:
			addContact(contactsList) # Pass super-list to all functions for updating
		
		# Display
		elif menuChoice == 2:
			displayContacts(contactsList)
		
		# Search
		elif menuChoice == 3:
			result = searchContacts(contactsList)
			print('')
			print("Here is your contacts information:")
			print(result) # Print list of requested contact info
			print('')

		# Edit
		elif menuChoice == 4:
			result = editContact(contactsList)
			if result == "There is no contact with that name in your address book.": # Validate output, does NOT append error message to super-list
				print("")
				print(result)
				print("")
			else:
				contactsList.append(result) # Append edited contact to super-list

		# Delete
		elif menuChoice == 5:
			deleteContact(contactsList)

		# Exit
		elif menuChoice == 6:
			repeat = False # End menu loop
			exitProgram(contactsList)

# Add
def addContact(contactsList): # Pass super-list to all functions for updating
	# Input Validation
	while True: 
			try:
				addNumber = int(input("How many contacts do you wish to add? ")) # Allows entry of multiple contacts
			except ValueError: # Asks for new menuChoice if input is not an integer
				print("Error: Please enter a digit.")
				continue
			if addNumber < 1: # Asks for new input if input is not a menu option
				print("Error: Please enter a digit greater than 0.")
				continue
			else: # If input is validation, input is accepted
				break
	
	for i in range(addNumber):
		# Request info for new contacts
		print("\r\nEnter information for contact #", i+1, sep='')
		name = str(input("\r\nName: "))
		address = str(input("\r\nAddress: "))
		phoneNumber = str(input("\r\nPhone Number: "))
		email = str(input("\r\nEmail: "))
		newContact = [name, address, phoneNumber, email] # Create list of new info
		contactsList.append(newContact) # Append new to list master list

	if addNumber < 2:
		print("\r\n", name, "has been added to your contacts.")
	else:
		print("\r\n Your", addNumber, "contacts have been added.") # confirmation to user

	return contactsList

# Display
def displayContacts(contactsList):
	print("")
	for chunk in range(len(contactsList)): # Chunk = nested lists
		for i in contactsList[chunk]: # i = items in chunks
			print(i) # Print list item
		print("") # Print space after each nested list

# Search
def searchContacts(contactsList):
	query = input("Who are you looking for? Enter their full name: ")

	for chunk in range(len(contactsList)):
		for i in contactsList[chunk]:
			if query == i:
				name = contactsList[chunk][0] # name is first line in each nested list, address is second, etc
				address = contactsList[chunk][1]
				phoneNumber = contactsList[chunk][2]
				email = contactsList[chunk][3]
				contact = [name, address, phoneNumber, email] # create sub-list
				return contact
			else:
				notFound = "There is no contact with that name in your address book."
	return notFound

# Edit
def editContact(contactsList):
	count = 0
	toEdit = str(input("Type the name of who you want to edit. Names are case sensitive: "))
	for chunk in range(len(contactsList)): # Chunk = nested lists
		for i in contactsList[chunk]: # i = items in chunks
			if toEdit == i: # if search query is found, find values of it and 3 lines below
				name = contactsList[chunk][0]
				address = contactsList[chunk][1]
				phoneNumber = contactsList[chunk][2]
				email = contactsList[chunk][3]

				# Menu
				print("1/ Name:", name)
				print("2/ Address:", address)
				print("3/ Phone Number:", phoneNumber)
				print("4/ Email:", email)
				print("5/ Return to menu.")

				repeat = True # Repeat menu until purposefully exited
				while repeat == True:
					choice = int(input("Which item would you like to edit? Enter its number: "))

					if choice == 1:
						name = input("New Name: ")
					elif choice == 2:
						address = input("New Address: ")
					elif choice == 3:
						phoneNumber = input("New Phone Number: ")
					elif choice == 4:
						email = input("New Email: ")
					elif choice == 5:
						repeat = False
						contactsList.pop(count) # Remove former contact
						newContact = [name, address, phoneNumber, email] # create sub-list with new contact
						contactsList.insert(count, newContact) # insert new contact to space where old existed
					else: 
						print("Please enter again.")
			else:
				result = "There is no contact with that name in your address book."
		count += 1 # increase count each loop to place new contact in same postion as old
	return result

# Delete
def deleteContact(contactsList):
	toDelete = input("Type the name of who you want to delete. Names are case sensitive: ")
	for chunk in range(len(contactsList)):
		for i in contactsList[chunk]:
			if toDelete == i:
				contactsList.remove(contactsList[chunk]) # If name exists in super-list, remove from super-list
				print("")
				print(toDelete, "has been deleted from your contacts.")
				print("")
				return contactsList
			else:
				notFound = "That name is not in your contacts."
	return notFound

# Exit
def exitProgram(contactsList):
	contacts = open("contacts.txt", "w") # Write super-list to .txt
	for chunk in contactsList:
		for i in chunk:
			print(i)
			contacts.write(i + '\r\n') # Write each item of nested list on new line
		print("") # After every nested list, create blank space
	contacts.close()



main() # Execute program