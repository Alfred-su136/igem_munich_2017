import scipy.integrate as spi
import numpy as np
import Plots
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


color_code=['#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21','#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21']
line_style=['-','.']
#result=[]

k_rpatx_lib=[0,0]

def ode_Cas13a(c, t, k, k_rpatx): 
    """170802LA, primitive kinetic model for Cas13a detection of target RNA
    and collateral RNase activity.
    concentrations in nM
    time in minutes """
    if c[2]>1000:
		c[2]=1000
#	if t<10:
#		k_rpatx=0
#	if 10<t<30:
#		k_rpatx=k_rpatx

    # single species
    Cas13a = c[0]; crRNA = c[1]; targetRNA = c[2]; collateralRNA = c[3];
    # complex species
    Cas13a_crRNA = c[4]; Cas13a_crRNA_targetRNA = c[5];
#    k_123=k_rpatx
   
    # rate constants   
    k_C13cr = k[0]; k_c13crtarget = k[1]; 
    # enzymatic rate constants
    k_c = k[2]; K_M = k[3];
    
    Cas13adot =  - k_C13cr*Cas13a*crRNA
    crRNAdot = - k_C13cr*Cas13a*crRNA
    
    Cas13a_crRNAdot = k_C13cr*Cas13a*crRNA - k_c13crtarget * targetRNA * Cas13a_crRNA
    targetRNAdot = - k_c13crtarget * targetRNA * Cas13a_crRNA+k_rpatx*targetRNA
    
    Cas13a_crRNA_targetRNAdot = k_c13crtarget * targetRNA * Cas13a_crRNA
    
    
    collateralRNAdot = - k_c * Cas13a_crRNA_targetRNA * collateralRNA/(K_M + collateralRNA) 
    
    return (Cas13adot,crRNAdot,targetRNAdot,collateralRNAdot,Cas13a_crRNAdot,
            Cas13a_crRNA_targetRNAdot)
    
    
    
fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax2 = fig.add_subplot(212)
ax1 = plt.subplot(111)
#ax2 = plt.subplot(212)


# Cas13a
'''

Define constants here. These come from plate reader experiments of Cas13a and 
afterwards fitting function to this. The reaction was done at 20 nM Cas13a and 
20 nM crRNA

'''
#k_C13cr = 1.0; k_c13crtarget = 0.1; k_c = 5; K_M = 20.0;
#k_C13cr = 0.000408423865267452; k_c13crtarget = 2782559.40220713; k_c = 1; K_M = 7.74263682681127
k_C13cr = 1.0; k_c13crtarget = 0.001; k_c = 10; K_M = 500.0
k0=(k_C13cr, k_c13crtarget, k_c, K_M) 

####
concentrations=[]
results=[]
for i in range(2,5):
#	k_rpatx=k_rpatx_lib[abc]
	for abc in range(0,2):
	    conc=1000*(10**(-i*1))
	    c0=(1,10,conc,185.0,0.0,0.0)
	    #k_rpatx=k_rpatx_lib[abc]
	    k_rpatx=k_rpatx_lib[abc]
    	
    	time = np.linspace(0,60,10000)
    	f1 = lambda y,t: ode_Cas13a(y, t, k0, k_rpatx)
    	sim = spi.odeint(f1,c0,time)
    
    # Dictionary for plotting afterwards
    	cdict={}
    	cdict['Cas13a']=sim[:,0]
    	cdict['crRNA']=sim[:,1]
    	collateralRNA = sim[:,3]
    	cdict['collateralRNA']=collateralRNA
    	cdict['Cas13a_crRNA']=sim[:,4]
    	cdict['Cas13a_crRNA_targetRNA']=sim[:,5]

    	datadict={'time': time, 'fluorescence': cdict}


#### Labeling for target RNA concentration loop
    	ax1.plot(time, collateralRNA,label='[targetRNA] = '+str(conc)+' nM',color=color_code[i],linewidth=2)
####
     
    
    
    	ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,frameon=False)
    	fluorescence=100*(cdict['collateralRNA'][0]-cdict['collateralRNA'][-1])/cdict['collateralRNA'][0]
#    	print(fluorescence)
    	results.append(fluorescence)
    	concentrations.append(conc)



#	ax2.plot(concentrations,results)

#plt.xscale('log')
#ax2.set_xlabel('Conc (nM)')
#ax2.set_ylabel('Fluorescence (%)')

ax1.set_xlabel('time (min)')
ax1.set_ylabel('RNAse Alert (nM)')
ax1.grid('on')
#print(fluorescence)
print(results)
print(concentrations)
plt.show()
