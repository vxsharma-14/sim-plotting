# script to show multiple plots in one image
# plot comparison of 4 plots of same sizes
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import matplotlib.gridspec as gridspec

m = 201
n = 201


#read data from file
print('\nReading data from the input file...')
x,y,ez1,ez2,ez3,ez4 = np.loadtxt('example.txt', delimiter='\t', unpack=True)

#assign fonts in the figure
plt.rc('font',family='serif',size=8)


#assign size of the plots and the resolution
fig,ax = plt.subplots(figsize=(10,8),dpi=150)

#command for reshaping data based on IM and JM
print('\nReshaping the input data file..')
X = np.reshape(x,(m,n))
Y = np.reshape(y,(m,n))
EZ1 = np.reshape(ez1,(m,n))
EZ2 = np.reshape(ez2,(m,n))
EZ3 = np.reshape(ez3,(m,n))
EZ4 = np.reshape(ez4,(m,n))

fname = ['Uniform 201x201 grid at t* ~ 0.15\ndt* = 6.0e-4, CN=0.2',
         'Uniform 201x201 grid at t* ~ 0.15\ndt* = 1.2e-3, CN=0.4',
         'Uniform 201x201 grid at t* ~ 0.15\ndt* = 1.5e-3, CN=0.5',
         'Uniform 201x201 grid at t* ~ 0.15\ndt* = 2.1e-3, CN=0.7']

for i in range (1,5):
    
    plt.subplot(2,2,i)

    #generate plot for the defined data
    print('\nGenerating data plot.')
    if i == 1:
        plt.pcolormesh(X,Y,EZ1,cmap='plasma',shading='gouraud')

    elif i == 2:
        plt.pcolormesh(X,Y,EZ2,cmap='plasma',shading='gouraud')

    elif i == 3:
        plt.pcolormesh(X,Y,EZ3,cmap='plasma',shading='gouraud')
        
    else:
        plt.pcolormesh(X,Y,EZ4,cmap='plasma',shading='gouraud')
    #define plot properties
    
    plt.xlabel('X (m)',size=10)
    plt.ylabel('Y (m)',size=10)
    plt.title(str(fname[i-1]),size=12)
    plt.xlim(0.2,0.5)
    plt.ylim(0.2,0.5)
    #specify colorbar title using the variable
    plt.clim(-0.08,0.09)
    plt.tight_layout()                                                      #trim unwanted whitespace in the figure
    cbar = plt.colorbar(format='%.0e')                                                   #assign a variable for colorbar
    cbar.set_label('Electric Field, Ez (V/m)',rotation=270,size=12,labelpad=15)
    #print('\nSaving figure in the "Working Folder"')
    #plt.savefig('New4.png',dpi=200)                        #save figure in "working folder"
    #print('\n***figure saved***')
    plt.gca().set_aspect('equal',adjustable='box')                          #sets the aspect ratio of the plot
   
plt.subplots_adjust(left=0.225,right=0.9,hspace=0.4,wspace=0.1)

plt.show()                                                              #show plot
