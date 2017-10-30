import os
from sys import version_info
py3 = version_info[0] > 2
import time

def question(a):
	if py3:
		while True:
			try:
				response1 = input('What would you like to do?')
			except ValueError:
				print("Please enter an integer")
			else:
				break
	else:
		while True:
			try:
				response1 = raw_input('What would you like to do?')
			except ValueError:
				print("Please enter an integer")
				continue
			else:
				break
#		response1 = raw_input("What would you like to detect?")
	return(response1)


print(
'''

###################################################################
#                                                                 #
#                        CascAID V1.0                             #
#                                                                 #
'''
+'#                   '+str(time.strftime("%c"))+'                      #'
'''				
#                                                                 #
#                      IGEM Munich 2017                           # 
#                                                                 #
#                                                                 #
#                                                                 #
#                                                                 #
#                  Please send bug reports to:                    #
#                                                                 #
#                         Sven Klumpe	                          #
#                                                                 #
#                E-Mail: sven.klumpe@tum.de                       #
#                                                                 #
###################################################################



###################################################################
##############        Welcome to CascAID         ##################
###################################################################



'''
)

x=1000
for i in range(0,20):
	print(
'''
#############               Main Menu            ################## 
					

[1] Access crRNA databank

[2] crRNA Secondary Structure Verification

[3] Evaluate off-target Effect of crRNA Design

[9] Exit Program
''')
	response1=question(i)
	try:
		x=int(response1)
	except ValueError:
		print('#####   Invalid Option. Please enter a valid option ######')
	if x==1:
		os.system('python ./python/db_execution.py')
	elif x==2:
		os.system('python ./python/secondary_structure_execution.py')
	elif x==3:
		os.system('python ./python/blast.py')
	elif x==9:
		exit()
	else:
		continue



