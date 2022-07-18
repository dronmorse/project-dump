#!/usr/bin/python3

import matplotlib.pyplot as plt

monodcon = 0.16
Kn = 0.010
Yxn = 31
Betamax = 0.3
Ks = 10
Yes = 0.47
kdprim = 0.0001


processlength = float(input("please give the length of the process: "))
timestep = float(input("please give the timestep: "))

timeout = []
nitrogenout = []
biomassout = []
sugarout = []
ethanolout = []

def winemaking(N,E,S,Xv):
    time = 0
    while time <= processlength-timestep:
        timeout.append(time)
        biomassout.append(Xv*30)
        nitrogenout.append(N*1000)
        sugarout.append(S)
        ethanolout.append(E)
        kd = kdprim*E
        monod = monodcon*N/(Kn+N)
        dXvdt = monod*Xv-kd*Xv
        Xv += dXvdt*timestep
        dNdt = -monod*Xv/Yxn
        N += dNdt*timestep
        Beta = Betamax*S/(Ks+S)
        dEdt = Beta*Xv
        E += dEdt*timestep
        dSdt = -Beta*Xv/Yes
        S += dSdt*timestep
        time += timestep
        if N < 0:
            N = 0
        if E < 0:
            E = 0
        if S < 0:
            S = 0
        if Xv < 0:
            Xv = 0
    return time 

proc = winemaking(0.15,0,240,0.2)
#N = 0.15 E = 0 S = 240 Xv = 0.1
print ("time of the process: ", proc)
plt.plot(timeout,nitrogenout, label = "nitrogen, mg/l")
plt.plot(timeout,biomassout, label = "biomass, g/l")
plt.plot(timeout,sugarout, label = "sugar, g/l")
plt.plot(timeout, ethanolout, label = "ethanol, g/l")
plt.legend(loc='upper right')
plt.show()

