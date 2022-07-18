#!/usr/bin/python3

from math import sin,exp,cos,pi
import matplotlib.pyplot as plt

ex = []

ey = []
edery = []

sinex = []

siney = []
cosy = []
sinedery = []

def expder(falsestart, step, end):
    exstep = falsestart
    while exstep < end :
        eystep = exp(exstep)
        exstep2 = exstep+step
        eystep2 = exp(exstep2)
        ex.append(exstep2)
        ey.append(eystep2)
        dydx = (eystep2-eystep)/(exstep2-exstep)
        edery.append(dydx)
        eystep = eystep2
        exstep = exstep2

def sinderx(falsestart, step, end):
    sinxstep = falsestart
    while sinxstep < end:
        sinystep = sin(sinxstep)
        sinxstep2 = sinxstep+step
        sinystep2 = sin(sinxstep2)
        sinex.append(sinxstep2)
        siney.append(sinystep2)
        dydx = (sinystep2-sinystep)/(sinxstep2-sinxstep)
        sinedery.append(dydx)
        sinystep = sinystep2
        sinxstep = sinxstep2
        cosystep = cos(sinxstep2)
        cosy.append(cosystep)

n = 80
m = 2*pi
#falsestart(dont change!), step, end
expder(0,2,n)
sinderx(-pi/10,pi/10,m)

expfunctx = []
expfuncty = []
const = 0
while const < n:
    expfunctx.append(const)
    expfuncty.append(exp(const))
    const += 0.01

cosfunctx = []
cosfuncty = []
const1 = 0
while const1 < m:
    cosfunctx.append(const1)
    cosfuncty.append(cos(const1))
    const1 += 0.01
    
sinfunctx = []
sinfuncty = []
const2 = 0
while const2 < m:
    sinfunctx.append(const2)
    sinfuncty.append(sin(const2))
    const2 += 0.01

plt.figure(1)
plt.plot(expfunctx,expfuncty,c='r',label=("exp(x)"))
plt.plot(ex,edery,c='g',label=("der(exp(x))"))
plt.legend(loc='upper left')
plt.xlim(70,85)

plt.figure(2)
plt.plot(sinfunctx,sinfuncty,c='r',label=("sin(x)"))
plt.plot(sinex,sinedery,c='g',label=("der(sin(x))"))
plt.plot(cosfunctx,cosfuncty,label=('cos(x)'))
plt.legend(loc='upper left')
plt.ylim(-1*1.5,1*1.5)
plt.xlim(0,4)

plt.show()
