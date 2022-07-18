#!/usr/bin/python3

import matplotlib.pyplot as plt
from math import exp,sin,pi,sqrt

x_in = [0,pi/6,pi/3,pi]
y_in = [1,sqrt(3)/2,1/2,-1]

def Neville(x,y):
    n = len(x)
    first = []
    firstx = []
    second = []
    secondx = []
    third = []
    thirdx = []
    y_out = []
    x_out = []

    #crude matrix construction
    for j in range(n):
        for i in range(n-j):
            #zero order, 4 values
            if j == 0:
                y_out.append(y[i])
                x_out.append(x[i])
            #first order, 3 values
            if j == 1:
                x_mid = (x[i+1]+x[i])/2
                p = ((x_mid-x[i+j])*y_out[i]+(x[i]-x_mid)*y_out[i+1])/(x[i]-x[i+j])
                first.append(p)            
                firstx.append(x_mid)
            #second order, 2 values
            if j == 2:
                x_mid = (x[i+1]+firstx[i+1])/2
                p = ((x_mid-x[i+j])*first[i]+(x[i]-x_mid)*first[i+1])/(x[i]-x[i+j])
                second.append(p)            
                secondx.append(x_mid)
            #third order, 1 value
            if j == 3:
                x_mid = (secondx[i+1]+firstx[i+1])/2
                p = ((x_mid-x[i+j])*second[i]+(x[i]-x_mid)*second[i+1])/(x[i]-x[i+j])
                third.append(p)            
                thirdx.append(x_mid)

    #x_out construction, values inserted in correct order

    o = 1
    for b in firstx:
        x_out.insert(o,b)
        o += 2

    p = 3
    for c in secondx:
        x_out.insert(p,c)
        p += 3

    for d in thirdx:
        x_out.insert(5,d)

    #y_out construction, values inserted in correct order

    q = 1
    for b in first:
        y_out.insert(q,b)
        q += 2

    e = 3
    for c in second:
        y_out.insert(e,c)
        e += 3

    for d in third:
        y_out.insert(5,d)

    print ('x values: ',x_out)
    print ('y values: ',y_out)
    return x_out, y_out

w = Neville(x_in,y_in)

plt.plot(w[0],w[1], c='g')
plt.scatter(x_in,y_in,marker='+',c='r')
plt.show()



