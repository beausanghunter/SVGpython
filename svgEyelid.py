#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:48:52 2022

@author: chrishunter
"""

import svgwrite
from svgpython import bezier
from svgpython import ovoidDefinitions
from svgpython import ovoid

filename = 'svgEyelid.svg'
dwg = svgwrite.Drawing(filename)

color = 'grey'
width=5
path = dwg.path(d='M 350,500 C 350,450 350,425 500,425 S 650,450 650,500 S 650,525 500,525 S 350,550 350,500')
#dwg.add(path.stroke(color=color,width=width).fill("none"))

center=(500,493)
ovoid_definition = ovoidDefinitions.OVOID_3.copy()
ovoid_definition['length'] *= .9
ovoid_definition['top_height'] *= .75 
ovoid_definition['bottom_height'] *= .75
ovoid_definition['top_scale'] *= .9
ovoid_definition['bottom_scale'] *= .9
ovoid_definition['side_scale'] *= .9
color='black'
fill='black'
width=1
scale = 1

ov3 = ovoid.Ovoid(dwg, center=center, ovoid_definition=ovoid_definition, color=color, width=width, fill=fill, scale=scale)

center=(500,485)
ovoid_definition = ovoidDefinitions.OVOID_3.copy()
ovoid_definition['length'] *= .75
ovoid_definition['top_height'] *= .5 
ovoid_definition['bottom_height'] *= .5
ovoid_definition['top_scale'] *= .75
ovoid_definition['bottom_scale'] *= .75
ovoid_definition['side_scale'] *= .75
color='white'
fill='white'
width=1
scale = 1

ov4 = ovoid.Ovoid(dwg, center=center, ovoid_definition=ovoid_definition, color=color, width=width, fill=fill, scale=scale)


# create the eyelid
color = 'red'
width=5
path = dwg.path(d='M 250,500 C 270,490 370,400 360,450 S 350,425 500,425 S 650,450 650,500 S 650,525 500,525 S 350,550 350,500')
#dwg.add(path.stroke(color=color,width=width).fill("none"))
r=5
fill='red'
#dwg.add(dwg.circle(center=(250,500),r=r, fill=fill))
#dwg.add(dwg.circle(center=(350,500),r=r, fill=fill))
#dwg.add(dwg.circle(center=(500,425),r=r, fill=fill))
#dwg.add(dwg.circle(center=(650,500),r=r, fill=fill))
#dwg.add(dwg.circle(center=(500,525),r=r, fill=fill))

fill='green'
#dwg.add(dwg.circle(center=(360,450),r=r, fill=fill))

color='red'
width=10
start = (250,500)
mid = (360,450)
end = (500,425)
start_tangent = (350,475)
mid1_tangent = (350,475)
mid2_tangent = (365,445)
end_tangent = (350,425)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color=color, width=width,end_points=False,tangents=False)

start = (250,500)
mid = (350,515)
end = (500,525)
start_tangent = (350,500)
mid1_tangent = (350,500)
mid2_tangent = (350,550)
end_tangent = (350,525)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color=color, width=width,end_points=False,tangents=False)

start = (750,500)
mid = (640,450)
end = (500,425)
start_tangent = (650,475)
mid1_tangent = (650,475)
mid2_tangent = (635,445)
end_tangent = (650,425)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color=color, width=width,end_points=False,tangents=False)

start = (750,500)
mid = (650,515)
end = (500,525)
start_tangent = (650,500)
mid1_tangent = (650,500)
mid2_tangent = (650,550)
end_tangent = (650,525)
b2 = bezier.bezier2(dwg, start, mid, end, start_tangent, mid1_tangent, mid2_tangent, end_tangent, color=color, width=width,end_points=False,tangents=False)

#dwg.add(dwg.line(start=(50,200), end=(50,150),stroke='red', stroke_width=3))
#dwg.add(dwg.line(start=(200,150), end=(150,150),stroke='red', stroke_width=3))
#dwg.add(dwg.line(start=(350,200), end=(350,150),stroke='red', stroke_width=3))
#dwg.add(dwg.line(start=(200,250), end=(250,250),stroke='red', stroke_width=3))


# Save the file
dwg.save()
