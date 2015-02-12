"""
Program is driven by a menu that allows users 
the ability to add/delete items based on calendar events
The events will be sortable by date
"""
import json

# Choose Number
print("""
-==Menu==-
1.) Create
2.) Delete
3.) Search
4.) Display
""")

# Get User's Choice
#choice = raw_input('>>')

class Item():

	def __init__(self):
		self.c_message = """
To Create an Item enter all relevant information.
This should include a <<Title>>, a <<Body>>, and a 
<<Priority Level>>
"""
		self.file_path = 'files/1_intermediate_save.json'

	def create_item(self):
		print(self.c_message)
		# New Item
		n_item = {}

		n_item['title'] = raw_input('Title: ')
		n_item['body'] = raw_input('Body: ')
		n_item['priority'] = raw_input('Priority: ')
		#print(item)

		with open(self.file_path, 'r+') as f:
			# Read Old Data
			data = json.loads(f.read())
			data.append(n_item)
			save_data = json.dumps(data)

			# Rewind file for writing
			f.seek(0)
			f.truncate()
			f.write("{0}\n".format(save_data))

	def show(self):
		with open(self.file_path, 'r') as f:
			item_list = json.loads(f.read())
		
		for i in item_list:
			print(i["title"])


item = Item()

#item.create_item()
item.show()