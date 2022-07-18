#!/usr/bin/python3

from math import exp,sin,cos,pi
import matplotlib.pyplot as plt

ex = []
sinx = []
cosx = []

ey = []
siny = []
cosy = []

trapintey = []
trapintsiny = []
trapintcosy = []

qintey = []
qintsiny = []
qintcosy = []

minuscosy = [] #unnecessary


def expint(start,step,jump,end):
    iters = 0
    trapinty = 0
    qinty = 0
    while start < end:
        trapinty += (jump-start)*0.5*(exp(start)+exp(jump))
        trapintey.append(trapinty)
        qinty += (jump-start)*exp((jump+start)/2)
        qintey.append(qinty)
        ex.append(jump)
        ey.append(exp(jump))
        start += step
        jump += step
        iters += 1
    return iters


def sinint(start,step,jump,end):
    iters = 0
    trapinty = 0
    qinty = 0
#???? -1 i działa, a bez -1 nie działa????????
    while start < end:
        trapinty += (jump-start)*0.5*(sin(start)+sin(jump))
        trapintsiny.append(trapinty-1)
        qinty += (jump-start)*sin((jump+start)/2)
        qintsiny.append(qinty-1)
        sinx.append(start)
        siny.append(sin(start))
        integral  = -cos(start)
        minuscosy.append(integral)
        start += step
        jump += step
        iters += 1
    return iters

def cosint(start,step,jump,end):
    iters = 0
    trapinty = 0
    qinty = 0
    while start < end:
        trapinty += (jump-start)*0.5*(cos(start)+cos(jump))
        trapintcosy.append(trapinty)
        qinty += (jump-start)*cos((jump+start)/2)
        qintcosy.append(qinty)
        cosx.append(start)
        cosy.append(cos(start))
        start += step
        jump += step
        iters += 1
    return iters

n = 10
m = 2*pi
#start,step,jump,end HERE TO CHANGE PARAMETERS
expint(0,2,2,n)
sinint(0,pi/(2.5),pi/(2.5),m)
cosint(0,pi/(2.5),pi/(2.5),m)

sumsin = 0
for i in siny:
    sumsin += i

sumexp = 0
for i in ey:
    sumexp += i

sumcos = 0
for i in cosy:
    sumcos += i

summinuscos = 0
for i in minuscosy:
    summinuscos += i

sumtrapsin = 0
for i in trapintsiny:
    sumtrapsin += i

sumsqrsin = 0
for i in qintsiny:
    sumsqrsin += i

sumtrapcos = 0
for i in trapintcosy:
    sumtrapcos += i

sumsqrcos = 0
for i in qintcosy:
    sumsqrcos += i

sumtrapexp = 0
for i in trapintey:
    sumtrapexp += i

sumsqrexp = 0
for i in qintey:
    sumsqrexp += i

expfunctx = []
expfuncty = []
const = 0
while const < n:
    expfunctx.append(const)
    expfuncty.append(exp(const))
    const += 0.01

minuscosfunctx = []
minuscosfuncty = []
const1 = 0
while const1 < m:
    minuscosfunctx.append(const1)
    minuscosfuncty.append(-cos(const1))
    const1 += 0.01
    
sinfunctx = []
sinfuncty = []
const2 = 0
while const2 < m:
    sinfunctx.append(const2)
    sinfuncty.append(sin(const2))
    const2 += 0.01

plt.figure("exp(x)", figsize=(5,5))
plt.plot(ex,trapintey,label=("trapint(exp(x)), sum = {}".format(sumtrapexp)))
plt.plot(ex,qintey,label=("squareint(exp(x)), sum = {}".format(sumsqrexp)))
#plt.plot(ex,ey,label=("int(exp(x)), sum = {}".format(sumexp)))
plt.plot(expfunctx,expfuncty,label=("int(exp(x)), sum = {}".format(sumexp)))
plt.legend(loc="upper left")
#plt.xlim(0,2)
#plt.ylim(0,10)

plt.figure("sin(x)", figsize=(5,5))
plt.plot(sinx,trapintsiny,label=("trapint(sin(x)), sum = {}".format(sumtrapsin)))
plt.plot(sinx,qintsiny,label=("squareint(sin(x)), sum = {}".format(sumsqrsin)))
#plt.plot(sinx,minuscosy,label=("int(sin(x)), sum = {}".format(summinuscos)))
plt.plot(minuscosfunctx,minuscosfuncty,label=("int(sin(x)), sum = {}".format(summinuscos)))
plt.legend(loc="upper left")
plt.ylim(-1,1)

plt.figure("cos(x)", figsize=(5,5))
plt.plot(cosx,trapintcosy,label=("trapint(cos(x)), sum = {}".format(sumtrapcos)))
plt.plot(cosx,qintcosy,label=("squareint(cos(x)), sum = {}, ".format(sumsqrcos)))
#plt.plot(cosx,siny,label=("int(cos(x)), sum = {}".format(sumsin)))
plt.plot(sinfunctx,sinfuncty,label=("int(cos(x)), sum = {}".format(sumsin)))
plt.legend(loc="upper left")
plt.ylim(-1,1)

#plt.figure("square(x)", figsize=(5,5))
#plt.plot(eqx,qintey,label=("qint(exp(x))"))
#plt.plot(eqx,eqy,label=("exp(x)"))
#plt.legend(loc="upper left")

#plt.figure("squarepsin(x)", figsize=(5,5))
#plt.plot(sinqx,qintsiny,label=("qint(sin(x))"))
#plt.plot(sinqx,sinqy,label=("sin(x)"))
#plt.legend(loc="upper left")

#plt.figure("squarecos(x)", figsize=(5,5))
#plt.plot(cosqx,qintcosy,label=("qint(cos(x))"))
#plt.plot(cosqx,cosqy,label=("cos(x)"))
#plt.legend(loc="upper left")


plt.show()


