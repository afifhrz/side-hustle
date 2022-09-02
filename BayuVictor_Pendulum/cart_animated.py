import numpy as np 

import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as pp
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

def accel_x (thetadot, xdot, theta):
    return (2*F+2*F*l**2*m-2*b*xdot-2*b*l**2*m*xdot+2*l**3*m**2*thetadot**2*np.sin(theta)+2*l*m*thetadot**2*np.sin(theta)+g*l**2*m**2*np.sin(2*theta))/(2*M+l**2*m**2+2*M*l**2*m+2*m-l**2*m**2*np.cos(2*theta))*mint

def accel_theta (thetadot, xdot, theta):
    return (-2*F*l*m*np.cos(theta)+2*b*l*m*xdot*np.cos(theta)-2*g*l*m**2*np.sin(theta)-2*M*g*l*m*np.sin(theta)-l**2*m**2*thetadot**2*np.sin(2*theta))/(2*M+l**2*m**2+2*M*l**2*m+2*m-l**2*m**2*np.cos(2*theta))*mint

# Crane Specification
F = 0
M = 5
b = 1

#pendulum_specification
m = 3.0
g = 9.8
mint = 12.0
l = 5.0
initial_angle = 90.0

# Time Step
initial_step = 0
h = 0.01
final_step = 2.0
t = np.arange(initial_step, final_step, h)
n = len(t) 

# theta punya
y=np.zeros(n)
y_v=np.zeros(n)
y[0] = np.radians(initial_angle) 
y_v[0] = np.radians(0.0)

# crane punya
x=np.zeros(n)
x_v=np.zeros(n)
x[0] = 0 
x_v[0] = 0

for i in range(0, n-1): 
    k1y = h*y_v[i]
    k1vy = h*accel_theta(y_v[i], x_v[i], y[i])

    k1x = h*x_v[i]
    k1vx = h*accel_x(y_v[i], x_v[i], y[i])

    k2y = h*(y_v[i]+0.5*k1vy)
    k2vy = h*accel_theta(y_v[i]+0.5*k1vy, x_v[i]+0.5*k1vx, y[i]+0.5*k1y)
    
    k2x = h*(x_v[i]+0.5*k1vx)
    k2vx = h*accel_x(y_v[i]+0.5*k1vy, x_v[i]+0.5*k1vx, y[i]+0.5*k1y)

    k3y = h*(y_v[i]+0.5*k2vy)
    k3vy = h*accel_theta(y_v[i]+0.5*k2vy, x_v[i]+0.5*k2vx, y[i]+0.5*k2y)
    
    k3x = h*(x_v[i]+0.5*k2vx)
    k3vx = h*accel_x(y_v[i]+0.5*k2vy, x_v[i]+0.5*k2vx, y[i]+0.5*k2y)

    k4y = h*(y_v[i]+k3vy)
    k4vy = h*accel_theta(y_v[i]+k3vy, x_v[i]+k3vx, y[i]+k3y)
    
    k4x = h*(x_v[i]+k3vx)
    k4vx = h*accel_x(y_v[i]+k3vy, x_v[i]+k3vx, y[i]+k3y)

    # Update next value of y 
    y[i+1] = y[i] + (k1y + 2 * k2y + 2 * k3y + k4y) / 6.0 
    y_v[i+1] = y_v[i] + (k1vy + 2 * k2vy + 2 * k3vy + k4vy) / 6.0

    # Update next value of x
    x[i+1] = x[i] + (k1x + 2 * k2x + 2 * k3x + k4x) / 6.0 
    x_v[i+1] = x_v[i] + (k1vx + 2 * k2vx + 2 * k3vx + k4vx) / 6.0

#canvas setting

fig, axs = pp.subplots(2,4)
gs = axs[1, 3].get_gridspec()

for ax in axs[-1,:4]:
    ax.remove()

axbig = fig.add_subplot(gs[-1, 0:])

fig.tight_layout()

#axbig setting
axbig.set_ylim(-5,20)
axbig.set_xlim(-5,50)
axbig.grid()
# axbig.set_aspect('equal')
patch = axbig.add_patch(Rectangle((0, 0), 0, 0, linewidth=1, edgecolor='k', facecolor='g'))

time_template = 'time = %.1fs'
time_text = axbig.text(0.05, 0.9, '', transform=axbig.transAxes)

cart_width = 2
cart_height = 2

line, = axbig.plot([], [], 'o-', lw=2)

axs[0,0].plot(t,x)
axs[0,0].set_title("Cart Motion")
axs[0,1].plot(t,x_v)
axs[0,1].set_title("Cart Velocity")
axs[0,2].plot(t,np.degrees(y))
axs[0,2].set_title("Pendulum Motion")
axs[0,3].plot(t,y_v)
axs[0,3].set_title("Pendulum Velocity")

def init():
    line.set_data([], [])
    time_text.set_text('')

    patch.set_xy((-cart_width/2, -cart_height))
    patch.set_width(cart_width)
    patch.set_height(cart_height)

    return line, time_text, patch

xs = x
pxs = l * np.sin(y) + xs
pys = l * np.cos(y)

def animate(i):
    thisx = [xs[i], pxs[i]]
    thisy = [0, pys[i]]
    time_text.set_text(time_template % (i*h))
    #draw axis
    patch.set_x(xs[i] - cart_width/2)
    line.set_data(thisx, thisy)

    return line, time_text, patch

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(x)),
                              interval=25, blit=True, init_func=init)

pp.show()

# # Set up formatting for the movie files
# print("Writing video...")
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=25, bitrate=1800)
# ani.save('controlled-cart.mp4', writer=writer)