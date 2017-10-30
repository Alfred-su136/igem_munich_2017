####### DATA BASE OF WANTED crRNA STRUCTURES ##### 
database_nupack=[
###### Structures from NUPACK RUNS#####
'(.((((((.((((.....)))).)))))).)', 
'(((..(((((......................)))))..)))',
'(.((((((.((((....)))).)))))).)',
'((((.(((....)))..))))',

#### STRUCTURE FROM CELL PAPER ####
'.....(((((.........))))..)....'
]


database_mfold=[
'(((((..............(((((((...............))))))).......)))))'
]



sequence_database={
# LWA BACKBONE
'lwaCas13a':'GAUUUAGACUACCCCAAAAACGAAGGGGACUAAAAC',
# LSH BACKBONE
'lbuCas13a':'GGAUAUAGACCACCCCAAUAUCGAAGGGGACUAAAAC',
# LBU BACKBONE
'lshCas13a':'GACCACCCCAAAAAUGAAGGGGACUAAAACA'
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
	j=0
	for structure in database_nupack:
		for result in results:
			if structure in result:
				if j==0:
					count=result.index(structure)
					print('NICE! YOU\'VE GOT THE RIGHT SECONDARY STRUCTURE!')
					print('YOUR SEQUENCE WAS:')
					print(sequence)
#					print('THE MATCHED SECONDARY STRUCTURE IS:')
					print(count*' ' + str(structure)+(len(result)-(1+count+len(structure)))*' ' +'    ######## MATCHED SECONDARY STRUCTURE')
					print(str(result[0:-2])+'     ######## PREDICTED SECONDARY STRUCTURE')
					j=j+1
			
	return()


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
				print('YOUR BACKBONE SEQUENCE HAS BEEN FOUND IN THE DATABANK')
				print('IT CORRESPONDS TO THE BACKBONE SEQUENCE OF: '+str(seq))
#				print(seq)
				j=j+1
		else:
			if k==len(sequence_database):
				print('BACKBONE STRUCTURE UNKNOWN, PLEASE HANDLE WITH CARE')
	return()
	
analysis_structure('input.tmp.subopt')
analysis_sequence('input.tmp.subopt')

