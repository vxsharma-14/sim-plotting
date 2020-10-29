'''script to display the animation of the results in 2-dimension
    for case: 5 and case: 7'''


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.rcParams['animation.ffmpeg_path']='C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe'
from matplotlib.animation import FuncAnimation

m = int(input('Enter IM ='))
n = int(input('Enter JM ='))
Ez = np.zeros([m,n])
#filenumber = np.linspace(10,150,15,dtype=int)
filenumber = np.linspace(10,200,20,dtype=int)

#assign fonts in the figure
plt.rc('font',family='serif',size=9)

def init():
    global fig, ax, im
    fig = plt.figure(figsize=(10,8))
    
    ax = plt.axes()
    ax.set_axis_off()
    #ax.set_xlim(0.0,0.6)
    #ax.set_ylim(0.0,0.6)
    #rect1 = patches.Rectangle((0.297,0.297),0.10,0.10,linewidth=1,
    #                          edgecolor='r',facecolor='none')
    #ax.add_patch(rect1)
    '''rect2 = patches.Rectangle((0.336,0.336),0.036,0.036,linewidth=1,
                              edgecolor='cyan',facecolor='none')
    ax.add_patch(rect2)'''
    im = ax.imshow(Ez, cmap='RdBu_r', interpolation='bilinear',
                   ,origin='lower',extent=[0,.6,0,.6])
    
    '''
    cbar = fig.colorbar(im,format='%.0e')
    cbar.set_label('Total Electric Field, Ez (V/m)',
                   rotation=270,size=12,labelpad=15)
    '''
    #im = ax.pcolormesh(X, Y, Ez, cmap='plasma', shading='gouraud')
    im.set_data(np.zeros(Ez.shape))
    return

def animate(i):
    print('var'+str(filenumber[i])+'.txt')
    x,y,ez = np.loadtxt('var'+str(filenumber[i])+'.txt',unpack=True)
    X = np.reshape(x,(m,n))
    Y = np.reshape(y,(m,n))
    Ez = np.reshape(ez,(m,n))
    #im.autoscale()
    im.set_data(Ez)
    
    return

init()
anim = FuncAnimation(fig, animate, frames=20,
                               interval=100, blit=False, repeat=False)
anim.save('two-d animation.mp4',fps=5,extra_args=['-vcodec', 'libx264'])
plt.tight_layout()

fig.show()
