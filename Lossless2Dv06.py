# script to show multiple plots in one image
# plot comparison of 4 plots of different grid sizes
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import matplotlib.gridspec as gridspec

m = 501
n = 501

m2 = 626
n2 = 626

m3 = 1001
n3 = 1001

m4 = 626
n4 = 626


#read data from file
print('\nReading data from the input file...')
x1,y1,ez1 = np.loadtxt('example.txt', delimiter='\t', unpack=True)
x2,y2,ez2 = np.loadtxt('example2.txt', delimiter='\t', unpack=True)
x3,y3,ez3 = np.loadtxt('example3.txt', delimiter='\t', unpack=True)
x4,y4,ez4 = np.loadtxt('example4.txt', delimiter='\t', unpack=True)

#assign fonts in the figure
plt.rc('font',family='serif',size=8)

#assign size of the plots and the resolution
fig,ax = plt.subplots(figsize=(10,8),dpi=150)

#command for reshaping data based on IM and JM
print('\nReshaping the input data file..')
X1 = np.reshape(x1,(m,n))
Y1 = np.reshape(y1,(m,n))
EZ1 = np.reshape(ez1,(m,n))

X2 = np.reshape(x2,(m2,n2))
Y2 = np.reshape(y2,(m2,n2))
EZ2 = np.reshape(ez2,(m2,n2))

X3 = np.reshape(x3,(m3,n3))
Y3 = np.reshape(y3,(m3,n3))
EZ3 = np.reshape(ez3,(m3,n3))

X4 = np.reshape(x4,(m4,n4))
Y4 = np.reshape(y4,(m4,n4))
EZ4 = np.reshape(ez4,(m4,n4))

fname = ['Uniform 101x101 grid at t* ~ 0.15\ndt* = 3.0e-3, CFL=0.5',
         'Uniform 201x201 grid at t* ~ 0.15\ndt* = 1.5e-3, CFL=0.5',
         'Uniform 501x501 grid at t* ~ 0.15\ndt* = 6.0e-4, CFL=0.5',
         'Uniform 626x626 grid at t* ~ 0.15\ndt* = 4.8e-4, CFL=0.5']

for i in range (1,4):
    plt.subplot(2,1,i)

    #generate plot for the defined data
    print('\nGenerating data plot.')
    if i == 1:
        #plt.pcolormesh(X1,Y1,EZ1,cmap='plasma',shading='gouraud')
        plt.contourf(X1,Y1,EZ1,cmap='plasma')

    elif i == 2:
        #plt.pcolormesh(X2,Y2,EZ2,cmap='plasma',shading='gouraud')
        plt.contourf(X2,Y2,EZ2,cmap='plasma')

    elif i == 3:
        #plt.pcolormesh(X3,Y3,EZ3,cmap='plasma',shading='gouraud')
        plt.contourf(X3,Y3,EZ3,cmap='plasma')
        
    else:
        #plt.pcolormesh(X4,Y4,EZ4,cmap='plasma',shading='gouraud')
        plt.contourf(X4,Y4,EZ4,cmap='plasma')
    #define plot properties
    
    plt.xlabel('X (m)',size=10)
    plt.ylabel('Y (m)',size=10)
    plt.title(str(fname[i-1]),size=10)
    plt.xlim(0.2,0.5)
    plt.ylim(0.2,0.5)
            #specify colorbar title using the variable
    plt.clim(-0.04,0.065)
    plt.tight_layout()                                                      #trim unwanted whitespace in the figure
    #cbar = plt.colorbar(format='%.0e')                                                   #assign a variable for colorbar
    #cbar.set_label('Electric Field, Ez (V/m)',rotation=270,size=12,labelpad=12)
    #print('\nSaving figure in the "Working Folder"')
    #plt.savefig('New4.png',dpi=200)                        #save figure in "working folder"
    #print('\n***figure saved***')
    plt.gca().set_aspect('equal',adjustable='box')                          #sets the aspect ratio of the plot
    
plt.subplots_adjust(left=0.225,right=0.9,hspace=0.4,wspace=0.1)

plt.show()                                                              #show plot
