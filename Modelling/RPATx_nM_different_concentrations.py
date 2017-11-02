import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#Standard color code
color_code=['#DEDEDE','#919191','#61A0D7','#3B7DBA','#74B845','#4C7F30','#C92717','#AE2317','#F6D428','#DBBD21']


#User input

#t_0=0
#t_end=600
#dt=1

half_time_RNA=33 #Minutes

# Constants calculations
RNA_hydro=-np.log(0.5)/(half_time_RNA*60)
#print RNA_hydro

#RNA0=8000




def amplification(t, y):


	RNAse=RNA_hydro
	Tx=(0.002/60)
	RPA=0.0008
	RT=0.5
# Assign some variables for convenience of notation
	RNA = y[0]
	DNA = y[1]

 
# Output from ODE function must be a COLUMN vector, with n rows
	n = len(y)	# 2: implies we have two ODEs
	dydt = np.zeros((n,1))
	dydt[0] = -RNAse*RNA+Tx*DNA
	dydt[1] = RPA*DNA+RT*RNA
	return dydt

#print amplification(10,[10,10]) 
nM_factor=(10**9)/((50*10**-6)*(6.022*10**23))

fig = plt.figure()

ax1 = plt.subplot(111)
fig.suptitle('Amplification of Target RNA', fontsize=20)
#ax2 = plt.subplot(122)

for x in range(1,9):
	nM=(10**-x)
#nM=0.01/16
	RNA0=nM/nM_factor
#	print RNA0
	# The ``driver`` that will integrate the ODE(s):
	if __name__ == '__main__':
 
 	    # Start by specifying the integrator:
	    # use ``vode`` with "backward differentiation formula"
	    r = integrate.ode(amplification).set_integrator('vode', method='bdf')
 
	    # Set the time range
	    t_start = 0
	    t_final = 6000
	    delta_t = 1
	    # Number of time steps: 1 extra for initial condition
	    num_steps = np.floor((t_final - t_start)/delta_t) + 1
 
	    # Set initial condition(s): for integrating variable and time!
	    RNA_t_zero = RNA0
	    DNA_t_zero = 0
	    r.set_initial_value([RNA_t_zero, DNA_t_zero], t_start)
 
	    # Additional Python step: create vectors to store trajectories
	    t = np.zeros((num_steps, 1))
	    RNA = np.zeros((num_steps, 1))
	    DNA = np.zeros((num_steps, 1))
	    t[0] = t_start
	    RNA[0] = RNA_t_zero
	    DNA[0] = DNA_t_zero
 
	    # Integrate the ODE(s) across each delta_t timestep
	    k = 1
	    while r.successful() and RNA[-1]*nM_factor<10:
	    #	    if RNA[-1]*nM_factor<10:
#	   	while r.successful() and k < num_steps:
#	        	print (RNA[r.t]*nM_factor)
	        r.integrate(r.t + delta_t)
	 
	       		 # Store the results to plot later
	       	t[k] = r.t
	        RNA[k] = r.y[0]
	        DNA[k] = r.y[1]
	        k += 1
 
 	   # All done!  Plot the trajectories in two separate plots:
	    
	    ax1.plot(t/60, RNA*nM_factor,label='$[Target RNA]_0$ = $10^{'+str(-x)+'}$ nM',color=color_code[x-1],linewidth=2)
	    ax1.set_xlim(t_start/60, 90)#t_final/60)
	    ax1.set_ylim(0,100)
	    ax1.set_yscale('log')
	    ax1.set_xlabel('time (min)')
	    ax1.set_ylabel('Target RNA (nM)')
	    ax1.grid(linestyle='-', linewidth=0.5)
 
	    
#	    DNA_global=[y*nM_factor for y in DNA]
#	    ax2.plot(t,DNA_global,label='[targetRNA] = 1e0'+str(x)+' nM')
#	    ax2.set_yscale('log')
#	    ax2.set_xlim(t_start, t_final)
#	    ax2.set_xlabel('Time (seconds)')
#	    ax2.set_ylabel('DNA (nM)')
#	    ax2.grid('on')

#formatter = plt.FuncFormatter(lambda ms, x: time.strftime('%M:%S', time.gmtime(ms // 1000)))
#ax1.xaxis.set_major_formatter(formatter)
treshold=[]
for i in range(0,len(t)):
	treshold.append('10')
ax1.plot(t/60,treshold,linestyle='-', color='r',linewidth=2)
ax1.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.show()    
    