import matplotlib.pyplot as plt
import random
import numpy as np
t0 = 0
t1 = 1000
V01 = random.randint(-80, -54)
V02 = random.randint(-80, -54)
tau_m = 20
tau_s = 10
El = -70
Vr = -80
Vt = -54
RI = 18
Rg = 0.15
dt = 0.1
Es = -80
P = 0.5

def D_s(s):
    return -s/tau_s

def dV_s(V,S):
   return (El-V+RI+Rg*(Es-V)*S)/tau_m

def synapse(dV_s,S):
    ts = [t0]
    Vs1 = [V01]
    Vs2 = [V02]
    s1 = 0
    s2 = 0
    t = t0
    V1=V01
    V2=V02
    
    while t<t1:
        s1 += D_s(s1)*dt
        s2 += D_s(s2)*dt
        N1 = dV_s(V1, s2)
        N2 = dV_s(V2, s1)
        V1+= N1 * dt
        V2+= N2 * dt        

        Vs1.append(V1 )
        Vs2.append(V2 )
        
        if V1 >= Vt:
             V1 = Vr
             s1 += P
        if V2 >= Vt:
            V2 = Vr
            s2 += P
        ts.append(ts[-1] + dt)
        t = t + dt
    return Vs1, Vs2, ts
Vs1,Vs2,ts = synapse(dV_s,D_s)
plt.plot(ts,Vs1,color='red',label='neuron1')
plt.plot(ts,Vs2,color='blue',label='neuron2')
plt.xlabel("t (ms)")
plt.ylabel("V(mv)")
plt.title("Excitatory with Es = -80mV")
plt.legend(loc=2)
plt.savefig('Q2_-80mA')
plt.show()