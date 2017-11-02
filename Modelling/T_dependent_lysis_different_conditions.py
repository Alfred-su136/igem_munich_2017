import numpy as np
import matplotlib.pyplot as plt


color_code=['#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21']
style=[' ','-',':','--','-.']
nM_factor=(10**9)/((50*10**-6)*(6.022*10**23))

#### User input

t_0=0
t_end=600
dt=1
ratio=30


#### Definition of Equations
def Baks_lysis(t):
	Baks=Baks0*np.exp(-B_lysis*t)
	return Baks
	
def RNA_from_lysis(t):
	RNA=((ratio*Baks0*B_lysis)/(B_lysis-RNA_hydro))*(np.exp(-RNA_hydro*t)-np.exp(-B_lysis*t))

	return RNA
	

#### RNase Equation for the moment where the Bacteria count drops under 1 and only 
#### RNA hydrolysis occurs
def RNAse(t,y):
	RNA=y*np.exp(-RNA_hydro*t)
	return RNA
	
#### Start for double Plotting of several Conditions
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
k=0



####### Change Loops to test different conditions here

####### Temperature loop; Comment out if not needed. Don't forget to Change Label!
for i in range(65,105,10):
	Temperature=i
	Temperature_K=273.15+Temperature
	k=k+1
####### If not Temperature Loop, set temperature here
#Temperature=95
#Temperature_K=273.15+Temperature

####### Initial Bacteria Count loop; Comment out if not needed. Don't forget to Change Label!
#for i in range(2,6):
#	Baks0=10**i
#	k=k+1
####### If not Bacteria Count loop, set initial Bacteria count here
	Baks0=1e02
	
	
	half_time_Baks_95=1.5 #Minutes; For Reference, see wiki page
	half_time_RNA=33 #Minutes; For Reference, See Wiki Page

	# Constants calculations
	B_lysis_95=-np.log(0.5)/(half_time_Baks_95*60)
	B_lysis=B_lysis_95*np.exp(-75984.6*((1/Temperature_K)-(1/368.15))/8.314)
	half_time_Baks_T=-np.log(0.5)/(B_lysis*60)
	RNA_hydro=-np.log(0.5)/(half_time_RNA*60)



	time=[]
	Baks=[]
	RNA=[]

	for t in range(t_0,t_end,dt):
		Bak=Baks_lysis(t)
		time.append(t)
		Baks.append(Bak)
		if Bak < 1:
			tt=t-len(time)
			y=RNA[-1]
			RNA.append(RNAse(-tt,y))
		else:
			RNA.append(RNA_from_lysis(t))
	time_min=[int(t)/60 for t in time]
	ax1.plot(time, Baks, color=color_code[k-1], linewidth=2, linestyle='--')
	ax1.set_xlabel('time (s)')
	ax1.set_ylabel('# Bacteria')
	RNA=[x*nM_factor*1e06 for x in RNA]
	
	
#### Change Plot Labelling here

####Labelling for Temperature
#	ax2.plot(time, RNA, color=color_code[k-1], linewidth=2, linestyle='-',label='T = '+str(i)+' $^\circ$C')
#	ax2.set_ylabel('target RNA (fM)')
####

####Labelling for Initial Bakteria Count
	ax2.plot(time, RNA, color=color_code[k-1], linewidth=2, linestyle='-',label='Baks$_0$ = $10^{'+str(i)+'}$')
	ax2.set_ylabel('target RNA (fM)')
####

ax1.grid('on')
ax2.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)
plt.show()

