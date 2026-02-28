#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 23:08:14 2022

@author: chrishunter
"""

import numpy as np
#import svgwrite
# Bezier data is stored in a 3x4 matrix where the columns are the points p0, p1, p2 and p3.  The bottom row is 1

class bezier:
    def __init__(self, dwg, m_bezier):
        self.m_bezier = m_bezier.copy()
        
    def transform(self, m_transform):
        self.m_bezier = np.matmul(m_transform,self.m_bezier)

    def print_matrix(self):
        print(self.m_bezier)
        
    def add_path(self, dwg, color='black', width=5, end_points=False, tangents=False, polyline=False):
        string_1 = 'M ' + str(self.m_bezier[0,0]) + ',' + str(self.m_bezier[1,0])
        string_2 = ' C ' + str(self.m_bezier[0,1]) + ',' + str(self.m_bezier[1,1])
        string_3 = ' ' + str(self.m_bezier[0,2]) + ',' + str(self.m_bezier[1,2])
        string_4 = ' ' + str(self.m_bezier[0,3]) + ',' + str(self.m_bezier[1,3])
#        string = string_1 + string_2 + string_3 + string_4
        path = dwg.path(d = string_1 + string_2 + string_3 + string_4 )
        dwg.add(path.stroke(color=color,width=width).fill('none'))
        if end_points:
            r=5
            fill='red'
            dwg.add(dwg.circle(center=(self.m_bezier[0,0],self.m_bezier[1,0]),r=r, fill=fill))
            dwg.add(dwg.circle(center=(self.m_bezier[0,3],self.m_bezier[1,3]),r=r, fill=fill))
        if tangents:
            stroke = 'blue'
            dwg.add(dwg.line(start=(self.m_bezier[0,0],self.m_bezier[1,0]), end=(self.m_bezier[0,1],self.m_bezier[1,1]),stroke=stroke, stroke_width=3))
            dwg.add(dwg.line(start=(self.m_bezier[0,2],self.m_bezier[1,2]), end=(self.m_bezier[0,3],self.m_bezier[1,3]),stroke=stroke, stroke_width=3))
#            dwg.add(dwg.line(start=end_tangent, end=end,stroke='blue', stroke_width=3))
        if polyline:
            r=5
            fill='red'
            stroke = 'blue'
            dwg.add(dwg.circle(center=(self.m_bezier[0,0],self.m_bezier[1,0]),r=r, fill=fill))
            dwg.add(dwg.circle(center=(self.m_bezier[0,1],self.m_bezier[1,1]),r=r, fill=fill))
            dwg.add(dwg.circle(center=(self.m_bezier[0,2],self.m_bezier[1,2]),r=r, fill=fill))
            dwg.add(dwg.circle(center=(self.m_bezier[0,3],self.m_bezier[1,3]),r=r, fill=fill))
            dwg.add(dwg.line(start=(self.m_bezier[0,0],self.m_bezier[1,0]), end=(self.m_bezier[0,1],self.m_bezier[1,1]),stroke=stroke, stroke_width=3))
            dwg.add(dwg.line(start=(self.m_bezier[0,1],self.m_bezier[1,1]), end=(self.m_bezier[0,2],self.m_bezier[1,2]),stroke=stroke, stroke_width=3))
            dwg.add(dwg.line(start=(self.m_bezier[0,2],self.m_bezier[1,2]), end=(self.m_bezier[0,3],self.m_bezier[1,3]),stroke=stroke, stroke_width=3))
            
        
    

class bezier2:
    def __init__(self, dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color='black', width=5,end_points=False,tangents=False):
        s = 'M ' + str(start[0]) + ',' + str(start[1])
        s += ' C ' + str(start_tangent[0]) + ',' + str(start_tangent[1])
        s += ' ' + str(mid1_tangent[0]) + ',' + str(mid1_tangent[1])
        s += ' ' + str(mid[0]) + ',' + str(mid[1])
        s += ' C ' + str(mid2_tangent[0]) + ',' + str(mid2_tangent[1])
        s += ' ' + str(end_tangent[0]) + ',' + str(end_tangent[1])
        s += ' ' + str(end[0]) + ',' + str(end[1])
        
        path = dwg.path(d = s)
        dwg.add(path.stroke(color=color,width=width).fill('none'))
        if end_points:
            r=5
            fill='red'
            dwg.add(dwg.circle(center=start,r=r, fill=fill))
            dwg.add(dwg.circle(center=mid,r=r, fill=fill))
            dwg.add(dwg.circle(center=end,r=r, fill=fill))
        if tangents:
            dwg.add(dwg.line(start=start, end=start_tangent,stroke='blue', stroke_width=3))
            dwg.add(dwg.line(start=mid1_tangent, end=mid,stroke='blue', stroke_width=3))
            dwg.add(dwg.line(start=mid2_tangent, end=mid,stroke='green', stroke_width=3))
            dwg.add(dwg.line(start=end_tangent, end=end,stroke='green', stroke_width=3))

