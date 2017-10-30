# igem_munich_2017


The folder db has to be downloaded externally since the Transcriptome databank exceeded the 25 MB limit for GitHub. Please find it here:
https://1drv.ms/f/s!AjkLLOd6IUjPhqA0dP3WyIem-GkIAg


INSTALLATION GUIDE

Please add the following to your .bashrc :


export BLASTHOME= ENTER BLAST HOME DIRECTORY HERE
export NUPACKHOME= ENTER NUPACK HOME DIRECTORY HERE
export NUPACKINSTALL=ENTER NUPACK HOME DIRECTORY HERE

alias blastx='$BLASTHOME/blastx'
alias blastn='$BLASTHOME/blastn'
alias makeblastdb='$BLASTHOME/makeblastdb'
alias blastn-short='$BLASTHOME/blastn-short'
#alias blastx='/Users/sven/Desktop/IGEM/Program/progress/blast/ncbi-blast-2.6.0+/bin/blastx'
#alias blastn='/Users/sven/Desktop/IGEM/Program/progress/blast/ncbi-blast-2.6.0+/bin/blastn'
#alias makeblastdb='/Users/sven/Desktop/IGEM/Program/progress/blast/ncbi-blast-2.6.0+/bin/makeblastdb'
#alias blastn-short='/Users/sven/Desktop/IGEM/Program/progress/blast/ncbi-blast-2.6.0+/bin/blastn-short'
export PATH=$PATH:$HOME/Desktop/IGEM/Program/progress/blast/ncbi-blast-2.6.0+/bin/

alias nupack_mfe='$NUPACKHOME/bin/mfe'
alias nupack_subopt='$NUPACKHOME/bin/subopt'
alias nupack_pfunc='$NUPACKHOME/bin/pfunc'
