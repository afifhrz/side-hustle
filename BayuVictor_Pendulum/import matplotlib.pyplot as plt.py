import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

# initialization function: plot the background of each frame
def init():
    fig = plt.figure()
    ax2 = fig.add_subplot(2, 1, 1)
    ax3 = fig.add_subplot(2, 1, 2)
    title = plt.title('')
    title.set_text('')
    return fig,ax2,ax3,title

# animation function.  This is called sequentially
def animate(i):

    a = ax2.pcolor(x,y,data)

    b = ax3.pcolor(x2,y2,data2)

    main_title.set_text('Main Title')
    title2.set_text('Sub title 1')
    title3.set_text('Sub title 2')

    return main_title, title2, title3, ax2, ax3

# call the animator.
fig = plt.figure()
ax2 = fig.add_subplot(2, 1, 1)
ax3 = fig.add_subplot(2, 1, 2)
title2 = ax2.set_title('')
title3 = ax3.set_title('')
main_title = fig.suptitle('')


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=101, interval=250, blit=False)
plt.show()