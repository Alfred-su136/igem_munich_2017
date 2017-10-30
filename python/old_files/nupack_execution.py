##### Script for running nupack with certain sequence ######

import sys
from nupack_programs import get_sequence, run_nupack_subopt
from nupack_analysis import analysis_structure


x=get_sequence()
run_nupack_subopt(x,1.5)
#analysis_structure('input.tmp.subopt')
