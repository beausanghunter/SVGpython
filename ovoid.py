#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 18:40:18 2022

@author: chrishunter
"""

import sys
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication#, QWidget

import svgwrite

# M sets the start point (absolute)

# c defines the a cubic Bezier
# c dx1 dy1, dx2 dy2, dx dy
# dx,dy is the end point
# dx1,dy1 controls the slope at the start of the curve
# dx2,dy2 controls the slope at the start of the curve

# s is a continuation of the cubic Bezier, starting with the same point as the previous one finished
# s dx2 dy2, dx dy
# dx,dy is the end point
# the slope at the start is the opposite of previous slope
# dx2,dy2 controls the slope at the start of the curve

# We draw the ovoid by starting on the left hand side and then going clockwise

class Ovoid:
    def __init__(self, dwg, center, ovoid_definition, color='black', width=0.2, fill='none', scale=1.0):

        length = ovoid_definition['length'] * scale
        top_height = ovoid_definition['top_height'] * scale
        bottom_height = ovoid_definition['bottom_height'] * scale
        top_scale = ovoid_definition['top_scale'] * scale
        bottom_scale = ovoid_definition['bottom_scale'] * scale
        side_scale = ovoid_definition['side_scale'] * scale
        
        center_x = center[0]
        center_y = center[1]

        self.center_x = center_x
        self.center_y = center_y
        self.length = length
        self.top_height = top_height
        self.bottom_height = bottom_height
        
        self.left = (center_x-length,center_y)
        self.right = (center_x+length,center_y)
        self.top = (center_x,center_y-top_height)
        self.bottom = (center_x,center_y+bottom_height)
        
        self.left_ref = (center_x-length,center_y-side_scale)
        self.right_ref = (center_x+length,center_y-side_scale)
        self.top_ref = (center_x-top_scale,center_y-top_height)
        self.bottom_ref = (center_x+bottom_scale,center_y+bottom_height)
        
        
        top_point = str(center_x) + ',' + str(center_y-top_height) # This is relative
        right_point = str(center_x+length) + ',' + str(center_y)
        bottom_point = str(center_x) + ',' + str(center_y+bottom_height)
        left_point = str(center_x-length) + ',' + str(center_y)        

        start_tangent = str(center_x-length) + ',' + str(center_y-side_scale)
        top_tangent = str(center_x-top_scale) + ',' + str(center_y-top_height)
        right_tangent = str(center_x+length) + ',' + str(center_y-side_scale)
        bottom_tangent = str(center_x+bottom_scale) + ',' + str(center_y+bottom_height)
        left_tangent = str(center_x-length) + ',' + str(center_y+side_scale)        
        
        start_string = 'M ' + left_point 
        q1_string = ' C ' + start_tangent + ' ' + top_tangent + ' ' + top_point 
        q2_string = ' S ' + right_tangent + ' ' + right_point 
        q3_string = ' S ' + bottom_tangent + ' ' + bottom_point 
        q4_string = ' S ' + left_tangent + ' ' + left_point 
        
        
        
        
        path_string = start_string + q1_string + q2_string + q3_string + q4_string
        print(path_string)
#path = dwg.path(d='M 50,500 c 0,5 155,50 150,50 s 150,0 150,-50 s -200,-50 -150,-50 s -150,0 -150,50')
        path = dwg.path(d=path_string)
        dwg.add(path.stroke(color=color,width=width).fill(fill))
        
    def add_circles(self,dwg,r=10,fill='red'):
        dwg.add(dwg.circle(center=(self.center_x-self.length,self.center_y),r=r, fill=fill))
        dwg.add(dwg.circle(center=(self.center_x,self.center_y-self.top_height),r=r, fill=fill))
        dwg.add(dwg.circle(center=(self.center_x+self.length,self.center_y),r=r, fill=fill))
        dwg.add(dwg.circle(center=(self.center_x,self.center_y+self.bottom_height),r=r, fill=fill))

        
    def add_tangents(self,dwg):
        dwg.add(dwg.line(start=self.left, end=self.left_ref,stroke='red', stroke_width=3))
        dwg.add(dwg.line(start=self.top, end=self.top_ref,stroke='red', stroke_width=3))
        dwg.add(dwg.line(start=self.right, end=self.right_ref,stroke='red', stroke_width=3))
        dwg.add(dwg.line(start=self.bottom, end=self.bottom_ref,stroke='red', stroke_width=3))
       
        