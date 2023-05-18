Total_tickets = 50
import re
def Count_ticket(Booked_tickets = 0):
	Remaining_tickets = Total_tickets - Booked_tickets
	return Remaining_tickets
print("welcome to the online booking portal")
booked_person = []
class details:
	def __init__(self, first_name, last_name, email, book_ticket):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.book_ticket = book_ticket
	def __repr__(self):
		return "details(first_name='{}', last_name='{}',email='{}', book_ticket='{}')".format(self.first_name, self.last_name, self.email, self.book_ticket)
	def __str__(self):
		return self.__repr__()
def booking(Remaining_tickets, Booked_tickets = 0):
	if (Remaining_tickets!=0):
		while (Remaining_tickets > 0):
			print("Book your ticket here to attend")
			first_name= input("enter the first name\n")
			last_name= input("enter the last name\n")
			email= input("enter the email\n")
			book_ticket= int(input("enter no of tickets\n"))
			if (re.match("[a-zA-z0-9_\-\.]+@[a-zA-Z]+\.(com|edu|net|in)", email) and ("[a-zA-z]{2,}", first_name) and ("[a-zA-z]{2,}", last_name)):
				if (0< book_ticket<=Remaining_tickets):
					user = details(first_name, last_name, email, book_ticket)
					print ("Thank you! {} {},for booking {} you will recieve confirmation mail on email {}".format(first_name, last_name, book_ticket, email))
					Booked_tickets = Booked_tickets + book_ticket		
					Remaining_tickets = Count_ticket(Booked_tickets)
					booked_person.append([user.first_name, user.last_name, user.email, user.book_ticket])
			else:
				print("invalid user details! try again")
			break
		print ("list of booking", booked_person)
		print("total tickcets are {} out of which {} are available ".format(Total_tickets, Remaining_tickets))
		Remaining_tickets = Count_ticket(Booked_tickets)
		booking(Remaining_tickets, Booked_tickets)
	else:
		print("Our booking is full! please visit next year")
Remaining_tickets = Count_ticket()
print("total tickcets are {}, {} tickets are available tickets ".format(Total_tickets, Remaining_tickets))
booking(Remaining_tickets)
