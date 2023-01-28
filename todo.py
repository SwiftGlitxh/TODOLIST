from time import sleep
import os

os.system('cls')
options = {"1": "Add Item", "2": "Remove Item", "3": "View ToDo lists"}
# Banner
def banner():
	# Clearing the Screen
		print('''
	 _______    _____        _      _     _   
	|__   __|  |  __ \\      | |    (_)   | |  
	   | | ___ | |  | | ___ | |     _ ___| |_ 
	   | |/ _ \\| |  | |/ _ \\| |    | / __| __|
	   | | (_) | |__| | (_) | |____| \\__ \\ |_ 
	   |_|\\___/|_____/ \\___/|______|_|___/\\__|
	   ---------------------------------------''')
while True:
	banner()
# Read file containing wordlist
	with open('wordlist.txt', 'r') as x: 
		lists = x.read()

# Print out Options
	for key in options:
		print(" ("+key + ") " + options[key])
# User input	
	choice = input("\n [+] Command >>  ")

# Add Item to TODO lists
	def add():
		item = input('[+] Add item to lists :')
		with open('wordlist.txt','a') as x:
			x.write('\n'+item)
		print(f'[=] \033[31m{item}\033[37m added to lists')
		input("\nPress Enter to continue...")
		os.system('cls')

# Remove Item to TODO lists
# ISSUE - If string not in lists > all words in file gets deleted ??
	def remove():
		print(lists)
		if len(lists) == 0:
			os.system('cls')
		else:	
			item = input('[-] Remove from lists: ')
			with open('wordlist.txt','w') as x:
				if item in lists:
					replaced = lists.replace(f'{item}', '')
					# Write
					x.write(replaced)
					os.system('cls')
				else:
					print(' "' + item+'" was not found in your lists')
					sleep(3)
					os.system('cls')
# View TODO lists 
	def todo():
		number = 0
		words = len(lists.split())
		if words < 1:
			print('[!] Your ToDo List Is Empty')
			a = input('[+] Would you like to add a item?')
			if a == 'yes':
				add()
			else:
				os.system('cls')
		else:
			print('TO DO lists\n----------')
			print(f'{lists}')
			input("Press Enter to continue...")
			os.system('cls')

# Results in option 1/2/3 picked.
	if choice == "1":
	    print("- You selected \033[31m" + options[choice] + "\033[37m\n")
	    add()
	elif choice == "2":
	    print("- You selected \033[31m" + options[choice] + "\033[37m\n")
	    remove()
	elif choice == "3":
	    print("- You selected \033[31m" + options[choice] + "\033[37m\n")
	    todo()
	else:
		os.system('cls')