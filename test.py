#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:50:09 2022

@author: chrishunter
"""

import numpy as np
import matplotlib.pyplot as plt


def check(p):
    c = np.array([15,25])
    r1_sq = (p[0]-c[0])**2 + (p[1]-c[1])**2
    print(r1_sq)
    tan = np.dot(p,c-p)
    print(tan)
#    dist_c = np.dot(p,p)+
    #print(dist_c1)
    
    
def plotC(r, p1, p2):
    x = []
    y = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    N = 101
    for i in range(N):
        theta = i / (N-1) * np.pi * 2.0
        x.append(r * np.cos(theta) + 15)
        y.append(r * np.sin(theta) + 25)
        x1.append(p1[0]/(N-1)*i)
        y1.append(p1[1]/(N-1)*i)
        x2.append(p2[0]/(N-1)*i)
        y2.append(p2[1]/(N-1)*i)

    plt.axes().set_aspect('equal')
    plt.xlim([0,25+r])
    plt.ylim([0,25+r])
    plt.plot(x,y,'r')
    plt.plot(x1,y1,'g')
    plt.plot(x2,y2,'g')
    plt.show()
    
p = [1.36, -36,150]
x = np.roots(p)
#print(x)
y = 30-0.6*x
#print(y)
p1 = np.array([ x[0], y[0]])
p2 = np.array([ x[1], y[1]])


x = 10
B = -25
C = x**2 - 15*x
p = [1, B, C]
y = np.roots(p)
#print(y)
y1 = y[0]
p1 = np.array([x,y1])
#check(p1)
y2 = y[1]
p2 = np.array([x,y2])
#check(p1)

for x in range(25):
    C = x**2 - 15*x
    p = [1, B, C]
    y = np.roots(p)
    r0 = (15-x)**2 + (25-y[0])**2
    r1 = (15-x)**2 + (25-y[1])**2
    print(x,y,r0,r1)

a1 = [ [21,18], [6,27] ]
a2 = [ [22,14], [2,26]]
plotC(np.sqrt(170),a2[0],a2[1] )    