import matplotlib.pyplot as plt
import math
import numpy as np
t0 = 0
t1 = 1000
V0 = -70
tau = 10
El = -70
Vr = -70
Vt = -40
Rm = math.pow(10, 10)
dt = 1

def dV(V,Ie):
   return (El-V+Rm*Ie)/tau

def euler(dV,t0,t1,V0,Vt,Vr,dt,Ie):
    ts = [t0]
    Vs = [V0]
    i = 0
    while ts[-1] <= t1:
        if Vs[-1] <= Vt:
            V = Vs[-1] + dV(Vs[-1],Ie)*dt
            ts.append(ts[-1] + dt)
            Vs.append(V)
        else:
            Vs[-1] = Vr
            i+=1
    spike = i
    return spike

I = np.linspace(2.0,5.0,31) * math.pow(10, -9)
spikes = []
for Ie in I:
    spike = euler(dV,t0,t1,V0,Vt,Vr,dt,Ie)
    spikes.append(spike)

plt.plot(I, spikes)
plt.xlabel("different current (mA)")
plt.ylabel("Firing Rate")
plt.title("Firing rate of different input current")
plt.savefig('Q3_3')
plt.show()
