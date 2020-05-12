#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import pearsonr

def linear(x,m,b):
    return m*x + b

def gaussian(x,A,sigma,mu):
    return A*np.exp(-0.5*((x-mu)/sigma)**2)

def two_gaussian(x,A1,sigma1,mu1,A2,sigma2,mu2):
    return (A1*np.exp(-0.5*((x-mu1)/sigma1)**2) +
            A2*np.exp(-0.5*((x-mu2)/sigma2)**2))

data = np.loadtxt('data.csv', delimiter=',')
t = data[:,0]
x = data[:,1]
y = data[:,2]

graphics = True#True to graph or False to not graph
bins = 15#Number of bins

###########################
## Is y a function of x? ##
###########################

xmin = min(x)
xmax = max(x)

partition = np.linspace(xmin,xmax,bins+1)#The partition is defined

for i in range(0,len(partition)-1):
    y_sample = []
    for j in range(0,len(x)):
        if partition[i] <= x[j] <= partition[i+1]:
            y_sample.append(y[j])
    frec, values, patches = plt.hist(y_sample,bins)
    vals = []
    for k in range(0,len(values)-1):
        vals.append((values[k]+values[k+1])/2)#Midle points are taken to fit
    try:
        popt, pcov = curve_fit(two_gaussian,vals,frec)
        vals = np.linspace(min(vals),max(vals),1000)
        plt.plot(vals,two_gaussian(vals,popt[0],popt[1],
                                   popt[2],popt[3],popt[4],popt[5]))
        fit = "Two Gaussians"
    except RuntimeError:
        try:
            popt, pcov = curve_fit(gaussian,vals,frec)
            vals = np.linspace(min(vals),max(vals),1000)
            plt.plot(vals,gaussian(vals,popt[0],popt[1],popt[2]))
            fit = "Gaussian"
        except RuntimeError:
            try:
                popt, pcov = curve_fit(linear,vals,frec)
                vals = np.linspace(min(vals),max(vals),1000)
                plt.plot(vals,linear(np.array(vals),popt[0],popt[1]))
                fit = "Linear"
            except RuntimeError:
                pass
    if graphics:
        plt.suptitle(str(partition[i])+" <= x <= "+str(partition[i+1]))
        plt.title("Fit: "+fit)
        plt.show()

###########################
## Is x a function of y? ##
###########################
    
ymin = min(y)
ymax = max(y)

partition = np.linspace(ymin,ymax,bins+1)#The partition is defined

for i in range(0,len(partition)-1):
    x_sample = []
    for j in range(0,len(y)):
        if partition[i] <= y[j] <= partition[i+1]:
            x_sample.append(x[j])
    frec, values, patches = plt.hist(x_sample,bins)
    vals = []
    for k in range(0,len(values)-1):
        vals.append((values[k]+values[k+1])/2)#Midle point
    try:
        popt, pcov = curve_fit(two_gaussian,vals,frec)
        vals = np.linspace(min(vals),max(vals),1000)
        plt.plot(vals,two_gaussian(vals,popt[0],popt[1],
                                   popt[2],popt[3],popt[4],popt[5]))
        fit = "Two Gaussians"
    except RuntimeError:
        try:
            popt, pcov = curve_fit(gaussian,vals,frec)
            vals = np.linspace(min(vals),max(vals),1000)
            plt.plot(vals,gaussian(vals,popt[0],popt[1],popt[2]))
            fit = "Gaussian"
        except RuntimeError:
            try:
                popt, pcov = curve_fit(linear,vals,frec)
                vals = np.linspace(min(vals),max(vals),1000)
                plt.plot(vals,linear(np.array(vals),popt[0],popt[1]))
                fit = "Linear"
            except RuntimeError:
                pass
    if graphics:
        plt.suptitle(str(partition[i])+" <= y <= "+str(partition[i+1]))
        plt.title("Fit: "+fit)
        plt.show()

#####################################
## Pearson correlation coefficient ##
#####################################

r = pearsonr(x,y)[0]
print("Pearson correlation coefficient =",r)
#plt.plot(x,y,'.')
#plt.show()
