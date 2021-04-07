import numpy as np
import math
import matplotlib.pyplot as plt



#v0 = [10(m/s)cos45 10(ms)sin45], X0 = [0,0]
#g = [0, -9.8]

m = 0.145 #kg, mass of baseball
g = np.array([0,-9.8]) #m/s^2acc of grave
rho = 1.225 #kg/m^3density of air
Cd = 0.47 #drag coo
A = 0.00414 #m^2 cross sectional area

def anal_proj_nodrag(t, init_pos=None, init_velo=None):
    times = t[:,np.newaxis]
    return init_pos +\
    init_velo*times +\
    g*0.5*times**2

def rk4(t, init_pos=None, init_velo=None, timestep): 
    y = init_pos
    h = timestep
    time = np.arange(0, t, h)
    ytimes = []
    for i in time:
        ytimes.append(y)
        k1 = h*init_velo(P=y)
        k2 = h*init_velo(P=y+0.5*k1)
        k3 = h*init_velo(P=y+0.5*k2)
        k4 = h*init_velo(P=y+0.5*k3)
        y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y


#def anal_proj_drag(t, init_pos=None, init_velo=None):
    

if __name__ == "__main__":
    print("test")
    times = np.arange(0, 10, 0.01)
    angle = 45*np.pi/180
    speed = 10
    V0 = speed*np.array([np.cos(angle), np.sin(angle)])
    X0 = np.array([0,0])
    positions = anal_proj_nodrag(times, init_pos=X0, init_velo=V0)

plt.plot(times, positions[:,0]) #for y position(x is 1)
plt.show()

