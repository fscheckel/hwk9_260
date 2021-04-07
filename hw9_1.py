import numpy as np
import matplotlib.pyplot as plt

#dp/dt=rP(1-(P/K))
#P(t)=(KP0e^(rt))/(K+P0(e^(rt)-1))

def analytic_solution(t, K=1, P0=1, r=0.01):
    """K = maximum carrying capacity of ecosystem
       P0 = initial population at time t=0
       r = population growth rate (eg, 1% = 0.01
       t = time """
    top = K*P0*np.exp(r*t)
    bottom = K+P0*(np.exp(r*t)-1)
    return top/bottom

def dP_dt(P, K=1, r=0.01):
    """P = population size
       r = population growth rate
       K = maximum capacity"""
    eco = r*P*(1-(P/K))
    return eco

def forward_euler(timestep = None,
                  max_time = None,
                  initial_time = None,
                  initial_val = None,
                  deriv = None, #pass dP_dt
                  deriv_params = None):
    """max_time = year 2300
       initial_time = year 1800
       initial_val = 1 (billion)
       deriv = """
    y = initial_val
    h = timestep
    times = np.arange(0, max_time, h)
    y_time = []
    for i in times:
        y = i + h * dP_dt(P=y)
        y_time.append(y)
    return times, y_time
    

def rk4(timestep = None,
        max_time = None,
        initial_time = None,
        initial_val = None,
        deriv = None,
        deriv_params = None):
    """max_time = year 2300
       initial_time = year 1800
       initial_val = 1 (billion)
       deriv = """
    y = initial_val
    h = timestep
    time = np.arange(0, max_time, h)
    ytimes = []
    for i in time:
        k1 = h*deriv(P=y)
        k2 = h*deriv(P=y+0.5*k1)
        k3 = h*deriv(P=y+0.5*k2)
        k4 = h*deriv(P=y+0.5*k3)
        y = i + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        ytimes.append(y)
    return time, ytime

if __name__ == "__main__":
    K = 10 #10 billion
    P0 = 1 #billion, population at year 1800
    r = 0.014 #1.4% growth rate
    start_year = 1800
    max_year = 2300
    max_time = max_year - start_year
    years_since_start = np.arange(0, max_time)

    analytic_sol = analytic_solution(years_since_start, K=K, P0=P0, r=r)
    timestep=25
    times,y_time = forward_euler(initial_val=P0, initial_time=0,
                             timestep=timestep,
                             max_time=max_time, deriv=dP_dt,
                             deriv_params={'K':K, 'r':r})

    times = times[:-2]
    y_time = y_time[:-2]

    #plt.scatter(times,y_time)#this is for euler
    #plt.scatter(time,ytime)#THIS IS FOR RK4
    plt.plot(analytic_sol)
    plt.xlabel('years(1800 - 2300)')
    plt.ylabel('population(billions)')
    plt.show()