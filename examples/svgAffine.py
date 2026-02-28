#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 00:02:41 2022

@author: chrishunter
"""

import svgwrite
from svgpython import bezier
import numpy as np

filename = 'svgAffine.svg'
dwg = svgwrite.Drawing(filename)


start = (100,100,1)
start_tangent = (125,125,1)
end_tangent = (125,175,1)
end = (100,200,1)
matrix_bezier = np.array( [ start, start_tangent, end_tangent, end ] ).T
#print(matrix_bezier)
b = bezier.bezier(dwg, matrix_bezier)
b.add_path(dwg, end_points=False, tangents=False)

# Translation
x_move = -100
y_move = -100
matrix_translate = np.array([ [1, 0, x_move], [0, 1, y_move], [0,0,1] ] )
b.transform(matrix_translate)
#b.print_matrix()


# Reflection
reflection = np.array([ [-1, 0, 0], [0, 1, 0], [0,0,1] ] )
#b.transform(reflection)
#b.print_matrix()


# Scale
x_scale = 1.5
y_scale = 1.5
scale = np.array([ [x_scale, 0, 0], [0, y_scale, 0], [0,0,1] ] )
#b.transform(scale)

# Rotation
theta  = np.pi / 4
cos_theta = np.cos(theta)
sin_theta = np.cos(theta)
rotation = np.array([ [cos_theta, -sin_theta, 0], [sin_theta, cos_theta, 0], [0,0,1] ] )
#b.transform(rotation)


# Reflection
reflection = np.array([ [-1, 0, 0], [0, 1, 0], [0,0,1] ] )
#b.transform(reflection)

# Shear
x_shear = 0.2
y_shear = 0.0
shear = np.array([ [1, x_shear, 0], [y_shear, 1, 0], [0,0,1] ] )
b.transform(shear)

# Translation
x_move = 100
y_move = 100
matrix_translate = np.array([ [1, 0, x_move], [0, 1, y_move], [0,0,1] ] )
b.transform(matrix_translate)


# Add the path
b.add_path(dwg, end_points=False, tangents=False, polyline=True)


# Save the file
dwg.save()

