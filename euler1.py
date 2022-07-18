#!/usr/bin/python3

from matplotlib import pyplot as plt
import math

step = float(input('give me the step for funct1: '))
#step2 = float(input('give me the step for funct2: '))
#step3 = float(input('give me the step for funct3: '))
#step4 = float(input('give me the step for funct4: '))
stepweird = float(input('give me the step for weird: '))

xout = []
yout = []

xout2 = []
yout2 = []

xout3 = []
yout3 = []

xout4 = []
yout4 = []

xeu = []
yeu = []

xeucheck = []
yeucheck = []

xweird = []
yweird = []

def funct1(x,y,der):
    while x < 5:
        xout.append(x)
        yout.append(y)
        x += step
        y = y + der*step
        der = y

def funct2(x2,y2,der2):
    while x2 < 5:
        xout2.append(x2)
        yout2.append(y2)
        x2 += step2
        y2 = y2 + der2*step2
        der2 = y2

def funct3(x3,y3,der3):
    while x3 < 5:
        xout3.append(x3)
        yout3.append(y3)
        x3 += step3
        y3 = y3 + der3*step3
        der3 = y3

def funct4(x4,y4,der4):
    while x4 < 5:
        xout4.append(x4)
        yout4.append(y4)
        x4 += step4
        y4 = y4 + der4*step4
        der4 = y4       

def exponential(xe,ye):
    while xe < 5:
        xeu.append(xe)
        yeu.append(ye)
        xe += 0.01
        ye = math.exp(xe)

def weird(x5,y5,dxdy):
        xweird.append(x5)
        yweird.append(y5)
        dxdy2 = y5+dxdy*stepweird
        avg = (dxdy+dxdy2)/2
        while x5 < 5:   
            y5 += avg
            xplus = x5 + stepweird
            dxdy2 += avg
            avg = (dxdy+dxdy2)/2
            x5 = xplus
            xweird.append(x5)
            yweird.append(y5)


     

funct1(0,1,1)
#funct2(0,1,1)
#funct3(0,1,1)
#funct4(0,1,1)
exponential(0,1)
weird(0,1,1)

plt.plot(xout,yout, 'r', label = "step = {}".format(step))
#plt.plot(xout2,yout2, 'g', label = "step = {}".format(step2))
#plt.plot(xout3,yout3, 'b', label = "step = {}".format(step3))
#plt.plot(xout4,yout4, 'c', label = "step = {}".format(step4))
plt.plot(xeu,yeu, 'k', label = "analytical solution")
plt.plot(xweird,yweird, 'm', label = "modified Euler's method, step = {}".format(stepweird))
plt.legend(loc='upper left')
plt.show()

    


