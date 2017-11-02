# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:40:55 2017

@author: ga25tur
"""
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plotKinetics(datadict, xlabel='Time (min)', ylabel='Fluorescence Intensity (a.u.)',
                 marker='.',filename='kinetics.png'):
    time=datadict['time']
    fluorescence=datadict['fluorescence']
    legend = list(fluorescence.keys())
    #f, axes = plt.
    for key in fluorescence:
        plt.plot(time, fluorescence[key],'.')
    plt.xlabel(xlabel,{"fontsize":16})
    plt.ylabel(ylabel,{"fontsize":16})
    #plt.yscale('log')
    plt.legend((legend),loc=0)
    plt.savefig(filename)
    plt.show()

def plotNullclines(X1,Y1,X2,Y2,trajectories={},legend=['xdot = 0','ydot = 0']):
    plt.plot(X1, Y1,'-')
    plt.plot(X2, Y2,'-')
    plt.xlabel('x',{"fontsize":16})
    plt.ylabel('y',{"fontsize":16})
    plt.legend((legend),loc=0)
    if trajectories != {}:
        fluorescence=trajectories['fluorescence']
        plt.plot(fluorescence['X'],fluorescence['Y'])
    plt.show()
    
def plotMultiKinetics(datadict, c, xlabel='Time', ylabel='Concentration',
                 marker='.'):
    time=datadict['time']
    fluorescence=datadict['fluorescence']
    f, axes = plt.subplots(1,7)
    cc=c
    for i in range(7):
        c=cc[i]
        axes[i].plot(time*c/max(cc), fluorescence['X'+str(c)],'.')
        axes[i].plot(time*c/max(cc), fluorescence['Y'+str(c)],'.')
        axes[i].set_xlabel(xlabel,{"fontsize":16})
        axes[i].set_ylabel(ylabel,{"fontsize":16})
        axes[i].legend(('x','y'),loc=0)
        axes[i].set_title('c = ' +str(c))
    plt.show()

#def plot3Dtrajectory(x, y, z, xlabel = 'x', ylabel = 'y', zlabel = 'z'):
#    fig = plt.figure()
#    ax = fig.gca(projection='3d')
#    ax.plot(x, y, z)    
#    ax.set_zlabel(zlabel)
#    ax.set_ylabel(ylabel)
#    ax.set_xlabel(xlabel)
#    plt.show()
