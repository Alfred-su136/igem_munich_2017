##### Script for running nupack with certain sequence ######

import sys, os
from secondary_structure_programs import get_sequence, run_nupack_mfe, run_nupack_subopt, run_mfold, run_nupack_pfunc, internet
from secondary_structure_analysis import analysis_structure, analysis_sequence, mfold_analysis


x=get_sequence()
#run_nupack_subopt(x,5)
run_nupack_mfe(x)
analysis_structure('input.tmp.mfe')
analysis_sequence('input.tmp.mfe')

y=internet()
if y==0:
	print('\n\nSince no internet connectivity available, mFOLD webserver was not considered.\n\n')
elif y==1:
	k=run_mfold(x)
	mfold_analysis(k)
os.system('rm input.tmp.mfe')