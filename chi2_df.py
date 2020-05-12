#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

###############
## Load data ##
###############

data = np.loadtxt('data.csv', delimiter=',')
t = data[:,0]
x = data[:,1]
y = data[:,2]

[Ax,ax,Bx,bx,Cx] = np.loadtxt("ajuste_x(t).txt")
[Ay,ay,By,by,Cy] = np.loadtxt("ajuste_y(t).txt")

######################
## Define functions ##
######################

def Chi2(observed, expected):
    """observed and expected are numpy's array"""
    return sum((observed - expected)**2/abs(observed))

def f(t,A,a,B,b,C):
    """Proposed function"""
    return A*np.cos(a*t) + B*np.cos(b*t) + C

##################
## Calculations ##
##################

Degrees_of_freedom = 5
chi2x = Chi2(x,f(t,Ax,ax,Bx,bx,Cx-4))/Degrees_of_freedom
chi2y = Chi2(y,f(t,Ay,ay,By,by,Cy-4))/Degrees_of_freedom

print("Chi² of fx:",chi2x)
print("Chi² of fy:",chi2y)
