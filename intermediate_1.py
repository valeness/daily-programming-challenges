"""
Program is driven by a menu that allows users 
the ability to add/delete items based on calendar events
The events will be sortable by date
"""
import json
from datetime import datetime

running = True

def menu():
	# Choose Number
	print("""
	-==Menu==-
	1.) Create
	2.) Delete
	3.) Search
	4.) Display
	5.) Quit
	""")

def get_choice():
	choice = raw_input('>>')
	return choice

class Item():

	def __init__(self):
		self.c_message = """
To Create an Item enter all relevant information.
This should include a <<Title>>, a <<Body>>, and a 
<<Priority Level>>
"""
		self.file_path = 'files/intermediate_1_save.json'

	def create_item(self):
		print(self.c_message)
		# New Item
		n_item = {}

		n_item['title'] = raw_input('Title: ')
		n_item['body'] = raw_input('Body: ')
		n_item['priority'] = raw_input('Priority: ')
		n_item['tags'] = raw_input('Tags: ')
		
		# Get Datetime after writing
		d_time = datetime.now()
		# Formatted Date and Time
		f_date = d_time.strftime("%d/%m/%y")
		f_time = d_time.strftime("%I:%M")
		# Store Date/Time as separate entities so we can use
		# split() on them when we are searching
		n_item['date'] = f_date
		n_item['time'] = f_time
		#print(item)

		with open(self.file_path, 'r+') as f:
			# Read Old Data
			data = json.loads(f.read())
			n_item['id'] = len(data)
			data.append(n_item)
			save_data = json.dumps(data)

			# Rewind file for writing
			f.seek(0)
			f.truncate()
			f.write("{0}\n".format(save_data))
		# Confirmation
		print("Item Created")

	def show(self):
		with open(self.file_path, 'r') as f:
			item_list = json.loads(f.read())
		
		print(
"""
 ID  | Title         | Body          | Tags          | Date          
"""
		)

		for i in item_list:
			print(" {5:3} | {0:13} | {1:13} | {2:13} | {3} {4}".format(i["title"], i["body"][:13], i["tags"][:13], i["date"], i["time"], str(i["id"])[:3]))

	def search(self):
		term = raw_input("Query: ")
		with open(self.file_path, 'r') as f:
			data = f.read()
			item_data = json.loads(data)

		for i in item_data:
			item_id = i["id"]
			title = i["title"]
			body = i["body"]

			if term.lower() in title.lower() or term.lower() in body.lower():
				print(
"""
ID: {0}
Title: {1}
Body: {2}""".format(item_id, title, body))

	def delete(self):
		print("Enter Id of the item you with to delete")
		select = int(raw_input('>>'))

		with open(self.file_path, 'r+') as f:
			data = f.read()
			item_data = json.loads(data)
			
			for i, v in enumerate(item_data):
				if v["id"] == select:
					del item_data[i]

			# Confirmation
			print("Deleted Successfully")

			data_save = json.dumps(item_data)

			# Rewind file for writing
			f.seek(0)
			f.truncate()
			f.write(data_save)



	def check_file(self):
		f = open(self.file_path, 'r+')
		r_file = f.read()
		if len(r_file) <= 2:
			# Rewind file for writing
			f.seek(0)
			f.truncate()
			f.write("[]")
			f.close()
		else:
			pass

item = Item()
item.check_file()

# 1.) Create
# 2.) Delete
# 3.) Search
# 4.) Display
# 5.) Quit

menu()
choice = get_choice()

while running:
	if '1' in choice:
		item.create_item()
		choice = get_choice()
	elif '2' in choice:
		item.delete()
		choice = get_choice()
	elif '3' in choice:
		item.search()
		choice = get_choice()
	elif '4' in choice:
		item.show()
		choice = get_choice()
	elif '5' in choice:
		print("Quitting")
		running = False
	elif 'h' in choice.lower():
		menu()
		choice = get_choice()