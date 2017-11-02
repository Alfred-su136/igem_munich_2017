# igem_munich_2017


The folder db has to be downloaded externally since the Transcriptome databank exceeded the 100 MB limit for GitHub. Please find it here:
https://1drv.ms/f/s!AjkLLOd6IUjPhqA0dP3WyIem-GkIAg
<br>
<br>
<br>
The program needs to be run from the home directory of the program. 

<br><br>
INSTALLATION GUIDE
<br>
If you run into problems during installation, please contact: 


Sven Klumpe;
<br>
iGEM Team Munich 2017;
<br>
E-Mail: sven.klumpe (at) tum.de


Required modules for installation are:<br>
biopython <br>
mechanize


You can install them typing following command: <br>
pip install biopython mechanize <br>
<br><br>
Please add the following to your .bashrc / .bash_profile:


export BLASTHOME= ENTER BLAST HOME DIRECTORY HERE<br>
export NUPACKHOME= ENTER NUPACK HOME DIRECTORY HERE<br>
export NUPACKINSTALL=ENTER NUPACK HOME DIRECTORY HERE<br>

alias blastx='$BLASTHOME/blastx'<br>
alias blastn='$BLASTHOME/blastn'<br>
alias makeblastdb='$BLASTHOME/makeblastdb'<br>
alias blastn-short='$BLASTHOME/blastn-short'<br>
export PATH=$PATH:$HOME/Desktop/IGEM/Program/progress/blast/ncbi-blast-2.6.0+/bin/<br>

alias nupack_mfe='$NUPACKHOME/bin/mfe'<br>
alias nupack_subopt='$NUPACKHOME/bin/subopt'<br>
alias nupack_pfunc='$NUPACKHOME/bin/pfunc'<br>


If you run into problems with the NUPACK and Blast binaries, please install them from their webpages. The installation guides can be found here: <br>
<br>
http://www.nupack.org/downloads
<br>
https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download
