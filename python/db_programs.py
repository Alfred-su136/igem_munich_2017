from sys import version_info
import sqlite3

py3 = version_info[0] > 2

def type(a,list):
	a=1
	Type=list
	print(
	'''
############             Choose your Target              #################
'''
)
	j=0
	for i in Type:
		j=j+1
		print('['+str(j)+'] ' + str(i))
	
	print(
'''
[0] Go back one step
'''
)
	
	if py3:
		while True:
			try:
				response1 = input("What would you like to detect?")
			except ValueError:
				print("Please enter an integer")
			else:
				break
	else:
		while True:
			try:
				response1 = raw_input("What would you like to detect?")
			except ValueError:
				print("Please enter an integer")
				continue
			else:
				break
	return(response1)

def target(a,list):
	print(
	'''
############         Available Detection Targets         #################
'''
)
	j=0
	for i in list:
		j=j+1
		print('['+str(j)+'] ' + str(i))
	
	print(
'''
[0] Go back one step
'''
)
	if py3:
		response2 = input("What would you like to detect?")
	else:
		response2 = raw_input("What would you like to detect?")
	return(response2)

def gene(a,list):
	print(
	'''
############             Choose your Target              #################
	''')
	j=0
	for i in list:
		j=j+1
		print('['+str(j)+'] ' + str(i))
	
	print(
'''
[0] Go back one step
'''
)


	if py3:
		response3 = input("What would you like to detect?")
	else:
		response3 = raw_input("What would you like to detect?")
	return(response3)
def sequence(a,list):
	print(
	'''
###########      The sequence thou art looking for is : ################
	''')
	j=0
	for i in list:
		j=j+1
		print(str(i))
	print(
'''
[1] Order from IDT

[9] Exit
[0] Go back one step
'''
)
	if py3:
		response4 = input("What would you like to do?")
	else:
		response4 = raw_input("What would you like to do?")
	return(response4)