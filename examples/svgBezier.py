#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 22:48:39 2022

@author: chrishunter
"""

import svgwrite
from svgpython import bezier

filename = 'svgs/svgBezier.svg'
dwg = svgwrite.Drawing(filename)

start = (100,100)
end = (100,200)
start_tangent = (125,125)
end_tangent = (125,175)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)

start = (100,125)
end = (100,175)
start_tangent = (112.5,137.5)
end_tangent = (112.5,162.5)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)


start = (200,100)
end = (200,200)
start_tangent = (250,150)
end_tangent = (250,150)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)

start = (300,100)
end = (300,200)
start_tangent = (325,125)
end_tangent = (350,150)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)

start = (400,100)
end = (400,200)
start_tangent = (425,150)
end_tangent = (450,125)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)

start = (100,300)
end = (100,400)
start_tangent = (125,325)
end_tangent = (125,375)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)

start = (200,300)
end = (200,400)
start_tangent = (175,275)
end_tangent = (225,375)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)

start = (300,300)
end = (300,400)
start_tangent = (250,250)
end_tangent = (250,450)
b = bezier.bezier(dwg, start, end, start_tangent, end_tangent,end_points=True,tangents=True)


start = (100,600)
mid = (200,500)
end = (300,600)
start_tangent = (125,600)
mid1_tangent = (200,525)
mid2_tangent = (200,525)
end_tangent = (275,600)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color='black', width=5,end_points=True,tangents=True)

start = (400,600)
mid = (500,500)
end = (600,600)
start_tangent = (450,600)
mid1_tangent = (500,550)
mid2_tangent = (500,550)
end_tangent = (550,600)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color='black', width=5,end_points=True,tangents=True)

start = (700,600)
mid = (800,550)
end = (900,500)
start_tangent = (750,575)
mid1_tangent = (750,575)
mid2_tangent = (800,525)
end_tangent = (850,500)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color='black', width=5,end_points=True,tangents=True)

start = (1100,600)
mid = (1000,575)
end = (1100,500)
start_tangent = (1050,600)
mid1_tangent = (1000,600)
mid2_tangent = (1000,500)
end_tangent = (1050,500)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color='black', width=5,end_points=True,tangents=True)

start = (600,400)
mid = (400,375)
end = (600,300)
start_tangent = (500,400)
mid1_tangent = (400,425)
mid2_tangent = (400,300)
end_tangent = (500,300)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color='black', width=5,end_points=True,tangents=True)

# Save the file
dwg.save()
