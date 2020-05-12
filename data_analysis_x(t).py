#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', delimiter=',')
t = data[:,0]
x = data[:,1]+4 #The data will be shifted 4 units to avoid negative values
y = data[:,2]

N = 10000 #length of range array to prove parameters

def Chi2(observed, expected):
    """observed and expected are numpy's array"""
    return sum((observed - expected)**2/abs(observed))

###########################
# 1. x as a function of t #
###########################

def fx(t,A,a,B,b,C):
    """Proposed function"""
    return A*np.cos(a*t) + B*np.cos(b*t) + C
print("\nProposed function: x(t) = A*cos(a*t) + B*cos(b*t) + C\n")

#Values estimated for the parameters of the proposed function
A_est = -1
a_est = 3
B_est = 2.2
b_est = 50
C_est = 4

#Variation of the parameter A

A_range = np.linspace(-2.3,0,N)
Chi2_x = []
for parameter in A_range:
    Expected = fx(t,parameter,a_est,B_est,b_est,C_est)
    Chi2_x.append(Chi2(x, Expected))

#plt.plot(A_range,Chi2_x)
#plt.xlabel("Parameter A",fontsize=20)
#plt.ylabel("$\chi^2$",fontsize=20)
#plt.grid()
#plt.show()
A = A_range[Chi2_x.index(min(Chi2_x))]
print("Parameter A:", A,
      "Evaluated in ["+str(A_range[0])+"; "+str(A_range[-1])+"]")

#Variation of the parameter a

a_range = np.linspace(2.8,3.2,N)
Chi2_x = []
for parameter in a_range:
    Expected = fx(t,A_est,parameter,B_est,b_est,C_est)
    Chi2_x.append(Chi2(x, Expected))

#plt.plot(a_range,Chi2_x)
#plt.grid()
#plt.show()
a = a_range[Chi2_x.index(min(Chi2_x))]
print("Parameter a:", a,
      "Evaluated in ["+str(a_range[0])+"; "+str(a_range[-1])+"]")

#Variation of the parameter B

B_range = np.linspace(0,3.6,N)
Chi2_x = []
for parameter in B_range:
    Expected = fx(t,A_est,a_est,parameter,b_est,C_est)
    Chi2_x.append(Chi2(x, Expected))

#plt.plot(B_range,Chi2_x)
#plt.grid()
#plt.show()
B = B_range[Chi2_x.index(min(Chi2_x))]
print("Parameter B:", B,
      "Evaluated in ["+str(B_range[0])+"; "+str(B_range[-1])+"]")

#Variation of the parameter b

b_range = np.linspace(49.8,50.2,N)
Chi2_x = []
for parameter in b_range:
    Expected = fx(t,A_est,a_est,B_est,parameter,C_est)
    Chi2_x.append(Chi2(x, Expected))

#plt.plot(b_range,Chi2_x)
#plt.grid()
#plt.show()
b = b_range[Chi2_x.index(min(Chi2_x))]
print("Parameter b:", b,
      "Evaluated in ["+str(b_range[0])+"; "+str(b_range[-1])+"]")

#Variation of the parameter C

C_range = np.linspace(4,4.1,N)
Chi2_x = []
for parameter in C_range:
    Expected = fx(t,A_est,a_est,B_est,b_est,parameter)
    Chi2_x.append(Chi2(x, Expected))

#plt.plot(C_range,Chi2_x)
#plt.grid()
#plt.show()
C = C_range[Chi2_x.index(min(Chi2_x))]-4#The parameter C is centered back
print("Parameter C:", C,
      "Evaluated in ["+str(C_range[0])+"; "+str(C_range[-1])+"]")

x = x-4#The x data are shifted -4 to turn back how they were originally

plt.suptitle("X AS A FUNCTION OF t",fontsize=25)
plt.plot(t,x,'.',label="Data")
LabelGraph = """Proposed function: X($t$) = Acos(a$t$) + Bcos(b$t$)
A = {}
a = {}
B = {}
b = {}
C = {}""".format(A,a,B,b,C)
plt.plot(t,fx(t,A,a,B,b,C),label=LabelGraph)
plt.xlabel("t (a.u.)",fontsize=20)
plt.ylabel("X (a.u.)",fontsize=20)
#plt.legend(loc="lower right")
plt.grid()
plt.show()

print('')
