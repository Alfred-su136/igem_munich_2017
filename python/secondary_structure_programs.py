import mechanize
from time import sleep
from sys import version_info
import os


py3 = version_info[0] > 2
RNA=['G','A','U','C','g','a','u','c']
DNA=['G','A','T','C','g','a','t','c']

def dna2rna_direct(sequence):
	'''
Input: DNA Sequence

Output: Direct RNA Sequence


Function that directly substitutes a DNA sequence with an RNA sequence. No transcriptional
complementarity involved!

	'''
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
	'''
Input: RNA sequence

Output: cDNA sequence

Reverse Transcription of RNA to cDNA.
	'''
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
	'''
Input: -

Output: Sequence

Asks for User's sequence Input
	'''
	tcount=0
	if py3:
		try:
			sequence_input = input("Please enter your crRNA sequence?")
		except ValueError:
			print("Please enter a valid sequence")
		sequence=str(sequence_input)
		sequence=sequence.upper()
		for i in range(0,len(sequence)):
			if sequence[i] not in RNA and sequence[i] not in DNA:
				print('Invalid sequence, please try again')
				break
			if sequence[i]=='T':
				print('\n\n\n!!!CAUTION!!! You entered a DNA sequence. This will be transcribed into RNA !!!CAUTION!!!\n')
	else:
		try:
			sequence_input = raw_input("Please enter your crRNA sequence?")
		except ValueError:
			print("Please enter a valid sequence")
		sequence=str(sequence_input)
		sequence=sequence.upper()
		for i in range(0,len(sequence)):
			if sequence[i] not in RNA and sequence[i] not in DNA:
				print('Invalid sequence, please try again')
				break
			if sequence[i]=='T':
				tcount=tcount+1
	if tcount > 0:
		print('\n\n\n!!!CAUTION!!! You entered a DNA sequence. This will be transcribed into RNA !!!CAUTION!!!')
		sequence=dna2rna_direct(sequence)
		#print(sequence)
	print(
	'''
#######################################################################################
#################### CascAID Secondary Structure Verification #########################
#######################################################################################



#######################################################################################
##################### NUPACK Secondary Structure Verification #########################
#######################################################################################
	'''
	)
	return(sequence.upper())

def run_nupack_mfe(sequence):
	'''
Input: RNA Sequence

Ouput: Minimal Free Energy in NUPACK file format

Writes Inputfile for minimal free energy calculation in NUPACK and executes it
	'''
	path=os.getcwd()
	sequence=sequence
	with open('input.tmp.in','w') as output_file:
		output_file.write('{0:2s}'.format(sequence))
	execute=path+'/programs/nupack3.2.1/build/bin/mfe input.tmp'
	os.system(execute)
#	os.system('rm input.tmp.in')
	return()
	
def run_nupack_subopt(sequence,sensitivity):
	'''
Input: RNA Sequence

Ouput: Secondary Structure and Free Energy of the most stable RNA Structures in NUPACK file format

Writes Inputfile for subopt calculation in NUPACK and executes it. Writes outputfile
	'''
	path=os.getcwd()
	sequence=sequence
	sensitivity=sensitivity
	with open('input.tmp.in','w') as output_file:
		output_file.write('{0:2s}'.format(sequence))
		output_file.write('\n{0:2f}'.format(sensitivity))
	execute=path+'/programs/nupack3.2.1/build/bin/subopt input.tmp'
	os.system(execute)
#	os.system('rm input.tmp.in')
	return()

def run_nupack_pfunc(sequence):
	'''
Input: RNA Sequence

Ouput: Partition Function in NUPACK file format

Writes Inputfile for pfunc calculation in NUPACK and executes it. Writes outputfile into directory
	'''
	path=os.getcwd()
	sequence=sequence
	with open('input.tmp.in','w') as output_file:
		output_file.write('{0:2s}'.format(sequence))
	execute=path+'/programs/nupack3.2.1/build/bin/pfunc input.tmp > input.tmp.pfunc'
	os.system(execute)
#	os.system('rm input.tmp.in')
	return()


def run_mfold(sequence):
	'''

Input: RNA sequence

Output: RNA sequence + Secondary Structure in Vienna Notation


Program that takes sequence and accesses mFOLD webserver to execute Secondary Structure
Prediction and returns the input sequence and the secondary structure in Vienna notation
	'''
	sequence=str(sequence)
	br=mechanize.Browser()
	br.open("http://unafold.rna.albany.edu/?q=mfold/rna-folding-form")
	br.select_form(name="FOLD")
	br.form["SEQ_NAME"]="mfold job"
	br.form["SEQUENCE"]=str(sequence)
	br.set_handle_robots(False)
	res=br.submit()
	content=res.readlines()
	for lines in content:
		if lines.startswith("        var refresh_url = "):
			new_url=lines[27:-16]
	sleep(30)

	results=br.open('http://unafold.rna.albany.edu'+str(new_url))

	br.open('http://unafold.rna.albany.edu'+str(new_url))
	i=0
	for link in br.links(text_regex='Vienna'):
#		print(link)
		result=br.follow_link(link)
		br._factory.is_html = True
		x=result.readlines()
	result2=results.readlines()
#	with open('result2.html','w') as output:
#		for lines in result2:
#			output.write(lines)
	return(x[0],x[1])
	
#print(run_mfold('GAUGGUAUCAUGUGGGUAUCAUA'))
def internet():
	if py3:
		for i in range(0,10):
			try:
				answer = input("Do you have internet connectivity? [yes/no]")
			except ValueError:
				print('Please enter a valid response')
			except NameError:
				print('Please enter a valid response')
			if not answer=='yes':
				if not answer=='no':
					continue
			if answer=='yes':
				return(1)
				break
			elif answer=='no':
				return(0)
				break
			else:
				continue
	else:
		while True:
			try:
				answer = raw_input("Do you have internet connectivity? [yes/no]")
				if answer=='yes':
					return(1)
				elif answer=='no':
					return(0)
				else:
					print('Please enter a valid response')
			except ValueError:
				print('Please enter a valid response')
			except NameError:
				print('Please enter a valid response')
			




#	if py3:
#		for i in range(0,10):
#			try:
#				answer = input("Do you have internet connectivity? [yes/no]")
#				if answer=='yes':
#					return(1)
#				elif answer=='no':
#					return(0)
#				else:
#					continue
#	for i in range(0,10):
#		try:
#			answer = input("Do you have internet connectivity? [yes/no]")
#			if answer=='yes':
#				return(1)
#			elif answer=='no':
#				return(0)
#			else:
#				continue
#		