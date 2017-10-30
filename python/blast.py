#import Bio
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from sys import version_info
from Bio.Blast.Applications import NcbiblastnCommandline
import os
import time

py3 = version_info[0] > 2
RNA=['G','A','U','C','g','a','u','c']
DNA=['G','A','T','C','g','a','t','c']

def dna2rna(sequence):
	sequence_input=str(sequence)
	sequence_output=''
	n=len(sequence_input)
	for i in range(0,n):
		if sequence_input[i]=='T':
			sequence_output=sequence_output+'A'
		elif sequence_input[i]=='A':
			sequence_output=sequence_output+'U'
		elif sequence_input[i]=='C':
			sequence_output=sequence_output+'G'
		elif sequence_input[i]=='G':
			sequence_output=sequence_output+'C'
		elif sequence_input[i]=='U':
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
	sequence_target=''
	if py3:		
		try:
			sequence_input = input("Please enter a RNA or cDNA sequence?")
		except ValueError:
			print("Please enter a valid sequence")
		sequence=str(sequence_input).capitalize()
		sequence_target=sequence[-28:]
		if len(sequence_target)<28:
			print('''
		#################### CAUTION! ##################### 
YOUR SEQUENCE IS SHORTER THAN THE USUAL 28 BP TARGET FOR crRNA DESIGNED FOR CAS13A
		#################### CAUTION! #####################\n\n ''')
		for i in range(0,len(sequence)):
			if sequence[i] not in RNA:
				if sequence[i] not in DNA:
					print('Invalid sequence, please try again')
					print(sequence[i])
			if sequence[i]=='U':
				tcount=tcount+1

	else:
		try:
			sequence_input = raw_input("Please enter a RNA or cDNA sequence?")
		except ValueError:
			print("Please enter a valid sequence")
		sequence=str(sequence_input).capitalize()
		sequence_target=sequence[-28:]
		if len(sequence_target)<28:
			print('''
		#################### CAUTION! ##################### 
YOUR SEQUENCE IS SHORTER THAN THE USUAL 28 BP TARGET FOR crRNA DESIGNED FOR CAS13A
		#################### CAUTION! #####################\n\n ''')
		for i in range(0,len(sequence)):
			if sequence[i] not in RNA:
				if sequence[i] not in DNA:
					print('Invalid sequence, please try again')
					print(sequence[i])
			if sequence[i]=='U':
				tcount=tcount+1
	
	if tcount > 0:
		print('!!!CAUTION!!! You entered a RNA sequence. This will be transcribed into DNA !!!CAUTION!!!')
		sequence=rna2cdna(sequence)
		sequence_target=sequence[-28:]
		if len(sequence_target)<28:
			print('''
		#################### CAUTION! ##################### 
YOUR SEQUENCE IS SHORTER THAN THE USUAL 28 BP TARGET FOR crRNA DESIGNED FOR CAS13A
		#################### CAUTION! #####################\n\n ''')
	return(sequence)



def run_blast(sequence,mode='blastn',database='nt',expect_thresh='0.1',identity_tresh='92',db='db/full_db.fa'):

#### DO FASTA FORMAT FOR BLASTING####
	a='>seq \n'
	sequence_target=sequence[-28:]
	a=a+sequence_target
	#print(a)
	
	
	with open('tmp.fasta','w') as tmp_file:
		tmp_file.write(a)
	
	
###### TO RUN ONLINE, CHANGE LINE HERE ##### 

#	result_handle=NCBIWWW.qblast("blastn", "nt", a,task="blastn-short")


###### TO RUN LOCALLY, CHANGE LINE HERE ######
	#blastn_cline = NcbiblastnCommandline(query="tmp.fasta", db=db, evalue=0.0001, outfmt=5, out="seq.xml")
	blastn_cline = NcbiblastnCommandline(query="tmp.fasta", db=db,  outfmt=5, out="seq.xml",task="blastn-short")
	blastn_cline()
	
	
###### TO READ FROM FILE, CHANGE LINE HERE #####
	result_handle = open("seq.xml")

	
	blast_record = NCBIXML.read(result_handle)
		
	
#	with open("my_blast.xml", "w") as out_handle:
#		out_handle.write(result_handle.read())
#	result_handle.close()
	
	IDENTITIES_VALUE_TRESH=16
	i=0
	with open('off_target.out','w') as output_file:
#		output_file.write('##################################################################\n')
#		output_file.write('####### Following possible off-targets have been identified ######\n')
#		output_file.write('##################################################################\n')
		output_file.write(
'''
##################################################################
############## CascAID Off-Target Effect Determination ###########
##################################################################



##################################################################
####################### Input Sequence ###########################
##################################################################

Your Sequence was:

'''
+sequence.upper()
+'Your target sequence thus is:'
+sequence_target.upper()
+'\n\n'
+str(time.strftime("%c"))
+'\n\n##################################################################\n\n\n'
+'''
##################################################################
####### Following possible off-targets have been identified ######
##################################################################
''')
		print(
'''
##################################################################
####################### Input Sequence ###########################
##################################################################

Your Sequence was:

'''
+sequence.upper()
+'\n\nYour target sequence thus is:\n'
+sequence_target.upper()
+'\n\n'
+str(time.strftime("%c"))
+'\n\n##################################################################\n\n\n'
+'''
##################################################################
####### Following possible off-targets have been identified ######
##################################################################
''')
		for alignment in blast_record.alignments:
			for hsp in alignment.hsps:
#				if hsp.expect > E_VALUE_THRESH:
					#print(hsp.expect)
				if hsp.identities > IDENTITIES_VALUE_TRESH:
#						print('****Alignment****')
#						print('>seq ' + str(i))
#						print('sequence:', alignment.title)
#						print('length:', alignment.length)
#						print('e value:', hsp.expect)
#						print('identity:',hsp.identities)
#						print(hsp.query[0:75] + '...')
#						print(hsp.match[0:75] + '...')
#						print(hsp.sbjct[0:75] + '...')
#						output_file.write('****Alignment**** \n')
					print('>seq ' + str(i))											
					print('sequence:' + str(alignment.title))
					print('length:' + str(alignment.length))	
					print('e value:' + str(hsp.expect))
					print('identity:' + str(hsp.identities))
					print(hsp.query[0:75] + '...')	
					print(hsp.match[0:75] + '...')
					print(hsp.sbjct[0:75] + '... \n')
						
					output_file.write('>seq ' + str(i)+'\n')											
					output_file.write('sequence:' + str(alignment.title) + '\n')
					output_file.write('length:' + str(alignment.length)+'\n')	
					output_file.write('e value:' + str(hsp.expect)+'\n')
					output_file.write('identity:' + str(hsp.identities)+'\n')
					output_file.write(hsp.query[0:75] + '... \n')	
					output_file.write(hsp.match[0:75] + '... \n')
					output_file.write(hsp.sbjct[0:75] + '... \n')
					i=i+1
		if i==0:
			print(
'''

No significant off-target effects have been identified!

''')
				
		print('___________________________________________________________\n')
		print('Job ended normally. '+str(time.strftime("%c")))
		print(
'''

These results have also been saved in:              off_target.out
The full BLAST output can be found in:                     seq.xml
'''	)

	return(a)
	
	
a=get_sequence()
run_blast(a)
os.system('rm tmp.fasta')

