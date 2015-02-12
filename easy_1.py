"""
Program that aks the user their name, age, and reddit handle.
Then read it back to them
Saves the information to JSON for easy retrieval
"""
import json

print("Enter Your Name Age and Reddit Username in the following format")
print("Name Age Reddit")

# Name Age Reddit (nar)
nar = raw_input(">>")

nar_list = nar.split(' ')
#print(nar_list)

message = """
Your name is <<{0}>> and you are <<{1}>> years old. 
You are known on reddit as <<{2}>>""".format(nar_list[0], nar_list[1], nar_list[2])
print(message)

print("Do you want to save this information? y/n")
print("This will overwrite the previous data")
choice = raw_input(">>")

if 'y' in choice:
	file_path = 'files/easy_1_save.json'
	with open(file_path, 'w') as f:
		save_data = json.dumps(nar_list)
		f.write(save_data)
		print("Successfully Saved to <<{0}>>".format(file_path))
else:
	print("Data was not saved")
