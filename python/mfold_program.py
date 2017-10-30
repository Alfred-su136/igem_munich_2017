import mechanize
from time import sleep

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
		print(link)
		result=br.follow_link(link)
		br._factory.is_html = True
		x=result.readlines()
	result2=results.readlines()
	with open('result2.html','w') as output:
		for lines in result2:
			output.write(lines)
	return(str(x[0])+"\n"+str(x[1]))
	
print(run_mfold('GAUGGUAUCAUGUGGGUAUCAUA'))
