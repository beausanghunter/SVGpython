#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 23:02:14 2022

@author: chrishunter
"""

import math

def bernstein_poly(n,i,u):
    return math.comb(n,i) * u**i * (1-u)**(n-i)


# Class to calculat a Bezier curve
# Initialise with n+1 points in a list p
class bezier_function():
    def __init__(self, p):
        self.n = p.len() - 1
        self.p = p.copy()
        
    def 