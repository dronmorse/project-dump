#!/usr/bin/python3

from random import random as rand
from math import sqrt, pi

def builtin(a):
    hit = 0
    total = 0
    for i in range(0,a):
        x = rand()
        y = rand()
        vect = sqrt(x**2+y**2)
        if vect <= 1:
            hit += 1
        total += 1
    pi = hit/total * 4        
    return pi

def lehmer(a,z,m,t):
    hit = 0
    total = 0
    for i in range (0,t):
        f = a*z%m
        x = f/m
        g = f*z%m
        y = g/m
        vect = sqrt(x**2+y**2)
        if vect <= 1:
            hit += 1
        total += 1
        a = g
    pil = hit/total * 4
    return pil

builtin = builtin(100000)
lehmer = lehmer(100,22,211,100000)
#lehmer = lehmer(16807,12369123,2147483647,10000)
berror = builtin-pi
lerror = lehmer-pi

print ("builtin rng pi is equal: ", builtin, "error is equal to: ", berror)
print ("lehmer rng pi is equal: ", lehmer, "error is equal to: ", lerror)
