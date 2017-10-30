from sys import version_info
import sqlite3
from db_programs import type, target, gene, sequence



##### ACCESSING DATABASE ######
db=sqlite3.connect(':memory:')
db=sqlite3.connect('./db/crRNA_db.db')


##### GREP ALL TYPES ########
cursor=db.cursor()
cursor.execute('''SELECT Type FROM IGEM''')
all_rows_type = cursor.fetchall()
#Type=[str(x[0]) for x in all_rows_type if all_rows_type.count(x) == 1]
Type=[str(x[0]) for x in all_rows_type]
Type=sorted(set(Type), key=Type.index)



#### GREP ALL STRAINS #######
for i in range(0,20):
	response1=target(1,Type)
	try:
		x=int(response1)
	except ValueError:
		print('Please enter an integer')
	if x==0:
		exit()
	else:
		try:
			cursor.execute('SELECT Strain FROM IGEM WHERE Type ="'+str(Type[int(response1)-1]+'"'))
			break
		except ValueError:
			continue
		except IndexError:
			print('Index out of range')
			continue

all_rows_strain=cursor.fetchall()
#Strain=[str(x[0]) for x in all_rows_strain if all_rows_strain.count(x) == 1]
Strain=[str(x[0]) for x in all_rows_strain]
Strain=sorted(set(Strain), key=Strain.index)


##### GREP ALL TARGETS ##### 
for i in range(0,20):
	response2=target(response1,Strain)
	try:
		x=int(response2)
	except ValueError:
		print('Please enter an integer')
	if x==0:
##### SAME CODE AS BEFORE ; GREP ALL STRAINS #####	
		for i in range(0,20):
			response1=target(1,Type)
			try:
				x=int(response1)
			except ValueError:
				print('Please enter an integer')
			if x==0:
				exit()
			else:
				try:
					cursor.execute('SELECT Strain FROM IGEM WHERE Type ="'+str(Type[int(response1)-1]+'"'))
					break
				except ValueError:
					continue
				except IndexError:
					print('Index out of range')
					continue
		all_rows_strain=cursor.fetchall()
#		Strain=[str(y[0]) for y in all_rows_strain if all_rows_strain.count(y) == 1]
		Strain=[str(x[0]) for x in all_rows_strain]
		Strain=sorted(set(Strain), key=Strain.index)
	else:
		try:
			cursor.execute('SELECT Target FROM IGEM WHERE Strain ="'+str(Strain[int(response2)-1]+'"'))
			break
		except ValueError:
			continue
		except IndexError:
			print('Index out of range')
			continue



##### GREP ALL TARGETS ##### 
cursor.execute('SELECT Target FROM IGEM WHERE Strain ="'+str(Strain[int(response2)-1]+'"'))
all_rows_targets=cursor.fetchall()
Targets=[str(x[0]) for x in all_rows_targets if all_rows_targets.count(x) == 1]
#print(Targets)
#response3=gene(response2,Targets)

for i in range(0,20):
	response3=gene(response2,Targets)
	try:
		x=int(response3)
	except ValueError:
		print('Please enter an integer')
	if x==0:
#### SAME CODE AS BEFORE ; GREP ALL TARGETS   ####
		for i in range(0,20):
			response2=target(response1,Strain)
			try:
				x=int(response2)
			except ValueError:
				print('Please enter an integer')
			if x==0:
		##### SAME CODE AS BEFORE ; GREP ALL STRAINS #####	
				for i in range(0,20):
					response1=target(1,Type)
					try:
						x=int(response1)
					except ValueError:
						print('Please enter an integer')
					if x==0:
						exit()
					else:
						try:
							cursor.execute('SELECT Strain FROM IGEM WHERE Type ="'+str(Type[int(response1)-1]+'"'))
							break
						except ValueError:
							continue
						except IndexError:
							print('Index out of range')
							continue
				all_rows_strain=cursor.fetchall()
#				Strain=[str(y[0]) for y in all_rows_strain if all_rows_strain.count(y) == 1]
				Strain=[str(x[0]) for x in all_rows_strain]
				Strain=sorted(set(Strain), key=Strain.index)
			else:
				try:
					cursor.execute('SELECT Target FROM IGEM WHERE Strain ="'+str(Strain[int(response2)-1]+'"'))
					break
				except ValueError:
					continue
				except IndexError:
					print('Index out of range')
					continue
		all_rows_targets=cursor.fetchall()
#		Targets=[str(y[0]) for y in all_rows_targets if all_rows_targets.count(y) == 1]
		Targets=[str(x[0]) for x in all_rows_targets]
		Targets=sorted(set(Targets), key=Targets.index)
	else:
		try:
			cursor.execute('SELECT Strain FROM IGEM WHERE Type ="'+str(Targets[int(response3)-1]+'"'))
			break
		except ValueError:
			continue
		except IndexError:
			print('Index out of range')
			continue

##### PRINT TARGET SEQUENCE ######

#### GREP ALL STRAINS #######
for i in range(0,20):
	cursor.execute('SELECT Sequence FROM IGEM WHERE Target ="'+str(Targets[int(response3)-1]+'"'))
	all_rows_sequences=cursor.fetchall()
	Sequence=[str(y[0]) for y in all_rows_sequences if all_rows_sequences.count(y) == 1]
	response4=sequence(response3,Sequence)
	try:
		x=int(response4)
	except ValueError:
		print('Please enter an integer')
	if x==0:
		for i in range(0,20):
			response3=gene(response2,Targets)
			try:
				x=int(response3)
			except ValueError:
				print('Please enter an integer')
			if x==0:
		#### SAME CODE AS BEFORE ; GREP ALL TARGETS   ####
				for i in range(0,20):
					response2=target(response1,Strain)
					try:
						x=int(response2)
					except ValueError:
						print('Please enter an integer')
					if x==0:
				##### SAME CODE AS BEFORE ; GREP ALL STRAINS #####	
						for i in range(0,20):
							response1=target(1,Type)
							try:
								x=int(response1)
							except ValueError:
								print('Please enter an integer')
							if x==0:
								exit()
							else:
								try:
									cursor.execute('SELECT Strain FROM IGEM WHERE Type ="'+str(Type[int(response1)-1]+'"'))
									break
								except ValueError:
									continue
								except IndexError:
									print('Index out of range')
									continue
						all_rows_strain=cursor.fetchall()
						Strain=[str(x[0]) for x in all_rows_strain]
						Strain=sorted(set(Strain), key=Strain.index)
					else:
						try:
							cursor.execute('SELECT Target FROM IGEM WHERE Strain ="'+str(Strain[int(response2)-1]+'"'))
							break
						except ValueError:
							continue
						except IndexError:
							print('Index out of range')
							continue
				all_rows_targets=cursor.fetchall()
				Targets=[str(x[0]) for x in all_rows_targets]
				Targets=sorted(set(Targets), key=Targets.index)
			else:
				try:
					cursor.execute('SELECT Strain FROM IGEM WHERE Type ="'+str(Targets[int(response3)-1]+'"'))
					break
				except ValueError:
					continue
				except IndexError:
					print('Index out of range')
					continue
	elif x == 9:
		break

db.close()