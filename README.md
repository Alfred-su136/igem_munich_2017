# igem_munich_2017


The folder db has to be downloaded externally since the Transcriptome databank exceeded the 100 MB limit for GitHub. Please find it here:
https://1drv.ms/f/s!AjkLLOd6IUjPhqA0dP3WyIem-GkIAg

The program needs to be run from the home directory of the program. 


INSTALLATION GUIDE

If you run into problems during installation, please contact: 


Sven Klumpe;
iGEM Team Munich 2017;
E-Mail: sven.klumpe (at) tum.de


Required modules for installation are:
biopython
mechanize


You can install them typing following command: 
pip install biopython mechanize

Please add the following to your .bashrc / .bash_profile:


export BLASTHOME= ENTER BLAST HOME DIRECTORY HERE
export NUPACKHOME= ENTER NUPACK HOME DIRECTORY HERE
export NUPACKINSTALL=ENTER NUPACK HOME DIRECTORY HERE

alias blastx='$BLASTHOME/blastx'
alias blastn='$BLASTHOME/blastn'
alias makeblastdb='$BLASTHOME/makeblastdb'
alias blastn-short='$BLASTHOME/blastn-short'
export PATH=$PATH:$HOME/Desktop/IGEM/Program/progress/blast/ncbi-blast-2.6.0+/bin/

alias nupack_mfe='$NUPACKHOME/bin/mfe'
alias nupack_subopt='$NUPACKHOME/bin/subopt'
alias nupack_pfunc='$NUPACKHOME/bin/pfunc'


If you run into problems with the NUPACK and Blast binaries, please install them from their webpages. The installation guides can be found here: 

http://www.nupack.org/downloads

https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download
