import time
####### DATA BASE OF WANTED crRNA STRUCTURES ##### 
database_nupack=[
###### Structures from NUPACK RUNS#####
'(((((.((.......)))))))....(((.....)))',
'(.((((((.((((.....)))).)))))).)', 
'(((((.((.......)))))))....((((...........))))',
#'(.((((((.((((....)))).)))))).)',
'...(((((.((.......)))))))....((((...........))))',
'...(((((.((.......)))))))....((((...........))))',
'((((((.........).)))))....((((...........))))',

#### lowest lbu backbone structure in NUPACK
'(((((.((.......)))))))....((((...........))))',
#### lowest lwa backbone structure in NUPACK
'((.(((((....((((.........)))).))))).))',

#### subopt lwa backbone alternative
'(((((....((((.........)))).)))))',

#### STRUCTURE FROM CELL PAPER ####
'.....(((((.........))))..)....'
]


database_mfold=[
#lwa backbone structure mfold
'((.(((((....((((.........)))).))))).))',
#lsh backbone structure mfold
'(((((...........)))))'
#lbu backbone structure mfold

#### Structure Lsh
'((((((((.((.......)))))))....((((...........))))'
]


sequence_database={
# LWA BACKBONE
'lwaCas13a':'GAUUUAGACUACCCCAAAAACGAAGGGGACUAAAAC',
# LSH BACKBONE
'lshCas13a':'GGAUAUAGACCACCCCAAUAUCGAAGGGGACUAAAAC',
# LBU BACKBONE
'lbuCas13a':'GACCACCCCAAAAAUGAAGGGGACUAAAACA'
}

####### ANALYSIS FUNCTIONS FOR NUPACK #####

def analysis_structure(inputfile):
	with open(inputfile,'r') as input_file:
		lines=input_file.readlines()
	i=0
	results=[]
	for line in lines:
		
		if line[0:3]=='% %':
			try:
				results.append(lines[i+3])
			except IndexError:
				continue
		if line.startswith('% Sequence:'):
			sequence=line[13:]
		i=i+1
	k=0
	j=0
	for structure in database_nupack:
		k=k+1
		for result in results:
			
#			print structure
#			print result
			if structure in result:
#				print(count*' ' + str(structure)+(len(result)-(1+count+len(structure)))*' ' +'    ########   MATCHED SECONDARY STRUCTURE')
#				print(str(result[0:-2])+'     ######## PREDICTED SECONDARY STRUCTURE')
				if j==0:
					count=result.index(structure)
					print('\nGOOD NEWS! YOU\'VE GOT THE RIGHT SECONDARY STRUCTURE!')
					print('YOUR SEQUENCE WAS:\n')
					print(sequence)
#					print('THE MATCHED SECONDARY STRUCTURE IS:')
					print(count*' ' + str(structure)+(len(result)-(1+count+len(structure)))*' ' +'    ########   MATCHED SECONDARY STRUCTURE')
					print(str(result[0:-2])+'     ######## PREDICTED SECONDARY STRUCTURE')
					j=j+1
			elif k==len(database_nupack):
				if j==0:
					print('''
		#################### CAUTION! ##################### 
		YOUR SECONDARY STRUCTURE DOES NOT FIT OUR DATA BANK
		#################### CAUTION! #####################\n\n ''')
					print('YOUR SEQUENCE AND MOST STABLE PREDICTED STRUCTURE IS:\n')
#				print(sequence)
#				print('THE PREDICTED MOST STABLE STRUCTURE IS:')
					print(sequence[0:-2])
					print(str(results[0][0:-2]))
				
			
	return()

def mfold_analysis(input):
	print('''

#######################################################################################
#################### MFOLD SECONDARY STRUCTURE VERIFICATION ###########################
#######################################################################################

''')
	sequence, structure_in = input
	result=structure_in[:-9]
	energy=structure_in[-10:-2]
	energy=energy.replace('\t','')
	energy=energy.replace('(','')
	energy=energy.replace(')','')
	energy=energy.replace(' ','')
#	print sequence
#	print result
#	print energy
	k=0
	j=0
	
	for structure in database_mfold:
		k=k+1
		if structure in result:
#				print(count*' ' + str(structure)+(len(result)-(1+count+len(structure)))*' ' +'    ########   MATCHED SECONDARY STRUCTURE')
#				print(str(result[0:-2])+'     ######## PREDICTED SECONDARY STRUCTURE')
			if j==0:
				count=result.index(structure)
				
				print('\nGOOD NEWS! mFOLD WEBSERVER CONFIRMS YOUR STRUCTURE')
				print('YOUR SEQUENCE WAS:\n')
				print(sequence)
#				print('THE MATCHED SECONDARY STRUCTURE IS:')
				print(count*' ' + str(structure)+(len(result)-(1+count+len(structure)))*' ' +'    ########   MATCHED SECONDARY STRUCTURE')
				print(str(result[0:-2])+'     ######## PREDICTED SECONDARY STRUCTURE')
				j=j+1
		elif k==1:
			if j==0:
				print('''
		#################### CAUTION! ##################### 
		mFOLD SECONDARY STRUCTURE DOES NOT FIT OUR DATA BANK
		#################### CAUTION! #####################\n\n''')
				print('YOUR SEQUENCE AND MOST STABLE PREDICTED STRUCTURE IS:\n')
#				print(sequence)
#				print('THE PREDICTED MOST STABLE STRUCTURE IS:')
				print(sequence[0:-2])
				print(str(result[0:-2]))
	print('______________________________________________________________________________________\n')
	print('Job ended normally. '+str(time.strftime("%c")))


def free_energy(inputfile):
	with open(inputfile,'r') as input_file:
		lines=input_file.readlines()
	i=0
	free_energies=[]
	for line in lines:
		
		if line[0:3]=='% %':
			try:
				free_energies.append(lines[i+2])
			except IndexError:
				continue
		i=i+1
	
			
	return()

def analysis_sequence(inputfile):
	with open(inputfile,'r') as input_file:
		lines=input_file.readlines()
	i=0
	for line in lines:
		
		if line.startswith('% Sequence:'):
			sequence=line[12:]
		i=i+1
	j=0
	k=0
	for seq in sequence_database:
#		print(seq)
		if  sequence_database[seq] in sequence:
			if j==0:
				print(len(sequence)*'_' + '\n')
				print( '		YOUR BACKBONE SEQUENCE HAS BEEN FOUND IN THE DATABANK')
				print( '		IT CORRESPONDS TO THE BACKBONE SEQUENCE OF: '+str(seq))
				print('______________________________________________________________________________________\n')
				print('Job ended normally. '+str(time.strftime("%c")))
#				print(seq)
				j=j+1
		else:
			if k==len(sequence_database):
				print('''
		#################### CAUTION! ##################### 
		BACKBONE STRUCTURE UNKNOWN, PLEASE HANDLE WITH CARE
		#################### CAUTION! #####################\n\n ''')
				print('______________________________________________________________________________________\n')
				print('Job ended normally. '+str(time.strftime("%c")))
	return()
	
	
	
#analysis_structure('input.tmp.subopt')
#analysis_sequence('input.tmp.subopt')


