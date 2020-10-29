# script to plot scattering from a lossless cylinder
# options included: plot total field and incident field on uniform grid
#                    in a single window
# imports properties from user defined function "colorbar" to match the size
# of plot and colorbar

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import matplotlib.gridspec as gridspec
from colorbar import colorbar

m = 626#int(input('Enter IM ='))
n = 626#int(input('Enter JM ='))
m2 = 626#int(input('Enter IM ='))
n2 = 626#int(input('Enter JM ='))

#read data from file
print('\nReading data from the input file...')
xc,yc,ezt = np.loadtxt('example.txt', delimiter='\t', unpack=True)
xn,yn,ezi = np.loadtxt('example2.txt', delimiter='\t', unpack=True)

#assign fonts in the figure
plt.rc('font',family='serif',size=9)

#assign size of the plots and the resolution
fig,ax = plt.subplots(figsize=(10,8),dpi=150)

#command for reshaping data based on IM and JM
print('\nReshaping the input data file..')
XC = np.reshape(xc,(m,n))
YC = np.reshape(yc,(m,n))
EZT = np.reshape(ezt,(m,n))
XN = np.reshape(xn,(m2,n2))
YN = np.reshape(yn,(m2,n2))
EZI = np.reshape(ezi,(m2,n2))

#assign fields as array objects
fields = ['EZ', 'EZI']
fname = ['E field on Uniform 626x626 grid \nCFL=0.5, STEPS=315, MRK',
         'E field on Uniform 626x626 grid \nCFL=0.5, STEPS=315, FDTD']

for i in range (1,3):
    plt.subplot(1,2,i)
    #cir1 = patches.Circle((0,0),0.2,edgecolor='b',facecolor='none')
    #ax.add_patch(cir1)

    #generate plot for the defined data
    print('\nGenerating data plot.')
    if i == 1:
        img1=plt.pcolormesh(XC,YC,EZT,cmap='plasma',shading='gouraud')
        colorbar(img1)    #sets colorbar properties for img1 from colorbar function
        #plt.contourf(XC,YC,EZT)
    else:
        img2=plt.pcolormesh(XN,YN,EZI,cmap='plasma',shading='gouraud')
        colorbar(img2)    #sets colorbar properties for img2 from colorbar function
        #plt.contourf(XN,YN,EZI)
    #define plot properties
    
    plt.xlabel('X (m)',size=10)
    plt.ylabel('Y (m)',size=10)
    plt.title(str(fname[i-1]),size=12)
    plt.xlim(0.2,0.5)
    plt.ylim(0.2,0.5)
    #cbar = plt.colorbar(format='%.0e')                                                   #assign a variable for colorbar
    #cbar.set_label('Electric Field, Ez',rotation=270,size=12,labelpad=15)        #specify colorbar title using the variable
    plt.clim(-1.0,1.0)
    plt.tight_layout(h_pad=1)                                                      #trim unwanted whitespace in the figure
    
    #print('\nSaving figure in the "Working Folder"')
    #plt.savefig('New4.png',dpi=200)                        #save figure in "working folder"
    #print('\n***figure saved***')
    plt.gca().set_aspect('equal',adjustable='box')                          #sets the aspect ratio of the plot

plt.show()                                                              #show plot
