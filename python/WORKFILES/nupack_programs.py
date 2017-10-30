from sys import version_info
import os



py3 = version_info[0] > 2
RNA=['G','A','U','C','g','a','u','c']
DNA=['G','A','T','C','g','a','t','c']

def dna2rna_direct(sequence):
	sequence_input=str(sequence)
	sequence_output=''
	n=len(sequence_input)
	for i in range(0,n):
		if sequence_input[i]=='T':
			sequence_output=sequence_output+'U'
		elif sequence_input[i]=='A':
			sequence_output=sequence_output+'A'
		elif sequence_input[i]=='C':
			sequence_output=sequence_output+'C'
		elif sequence_input[i]=='G':
			sequence_output=sequence_output+'G'
		elif sequence_input[i]=='U':
			print('Error, DNA and RNA mixed!')
			sequence_output=sequence_output+'U'
		else:
			continue
		
	return(sequence_output)
	
def rna2cdna(sequence):
	sequence_input=str(sequence)
	sequence_output=''
	n=len(sequence_input)
	for i in range(0,n):
		if sequence_input[i]=='T':
			print('Error, DNA and RNA mixed!')
			sequence_output=sequence_output+'A'
		elif sequence_input[i]=='A':
			sequence_output=sequence_output+'U'
		elif sequence_input[i]=='C':
			sequence_output=sequence_output+'G'
		elif sequence_input[i]=='G':
			sequence_output=sequence_output+'C'
		elif sequence_input[i]=='U':
			sequence_output=sequence_output+'A'
		else:
			continue
	sequence_output_reverse=sequence_output[::-1]
		
	return(sequence_output_reverse)
		
def get_sequence():
	tcount=0
	if py3:
		try:
			sequence_input = input("Please enter an RNA sequence?")
		except ValueError:
			print("Please enter a valid sequence")
		sequence=str(sequence_input)
		sequence=sequence.upper()
		for i in range(0,len(sequence)):
			if sequence[i] not in RNA and sequence[i] not in DNA:
				print('Invalid sequence, please try again')
			if sequence[i]=='T':
				print('!!!CAUTION!!! You entered a DNA sequence. This will be transcribed into RNA !!!CAUTION!!!')
				

	else:
		try:
			sequence_input = raw_input("Please enter an RNA sequence?")
		except ValueError:
			print("Please enter a valid sequence")
		sequence=str(sequence_input)
		sequence=sequence.upper()
		for i in range(0,len(sequence)):
			if sequence[i] not in RNA and sequence[i] not in DNA:
				print('Invalid sequence, please try again')
			if sequence[i]=='T':
				tcount=tcount+1
	if tcount > 0:
		print('!!!CAUTION!!! You entered a DNA sequence. This will be transcribed into RNA !!!CAUTION!!!')
		sequence=dna2rna_direct(sequence)
		print(sequence)
	return(sequence.upper())
#print(get_sequence(1))

def run_nupack_mfe(sequence):
	path=os.getcwd()
	sequence=sequence
#	parent = Path(__file__).resolve().parent
	with open('input.tmp.in','w') as output_file:
		output_file.write('{0:2s}'.format(sequence))
	execute=path+'/nupack3.2.1/build/bin/mfe input.tmp'
	os.system(execute)
#	os.system('rm input.tmp.in')
	return path
	
def run_nupack_subopt(sequence,sensitivity):
	path=os.getcwd()
	sequence=sequence
	sensitivity=sensitivity
#	parent = Path(__file__).resolve().parent
	with open('input.tmp.in','w') as output_file:
		output_file.write('{0:2s}'.format(sequence))
		output_file.write('\n{0:2f}'.format(sensitivity))
	execute=path+'/nupack3.2.1/build/bin/subopt input.tmp'
	os.system(execute)
#	os.system('rm input.tmp.in')
	return path

def run_nupack_pfunc(sequence):
	path=os.getcwd()
	sequence=sequence
#	sensitivity=sensitivity
#	parent = Path(__file__).resolve().parent
	with open('input.tmp.in','w') as output_file:
		output_file.write('{0:2s}'.format(sequence))
#		output_file.write('\n{0:2f}'.format(sensitivity))
	execute=path+'/nupack3.2.1/build/bin/pfunc input.tmp > input.tmp.pfunc'
	os.system(execute)
	os.system('rm input.tmp.in')
	return path



	
#x=get_sequence()
#run_nupack_mfe(x)
#run_nupack_subopt(x,1.5)
#run_nupack_pfunc(x)


	

	
