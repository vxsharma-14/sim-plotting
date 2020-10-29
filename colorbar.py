''' function to control the colorbar properties
it takes one arguement as input
'''

def colorbar(mappable):
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    import matplotlib.pyplot as plt
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax,format='%.0e')
    #cbar = plt.colorbar(format='%.0e')                                                   #assign a variable for colorbar
    cbar.set_label('Electric Field, Ez (V/m)',rotation=270,size=12,labelpad=15)
    plt.sca(last_axes)
    return cbar
