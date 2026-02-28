#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:45:41 2022

@author: chrishunter
"""

import sys
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication#, QWidget

import svgwrite
from svgpython import ovoid
from svgpython import ovoidDefinitions


filename = 'svgs/svgwrite-example6.svg'
dwg = svgwrite.Drawing(filename)
        
# set the variables for the ovoid
center = (600,200)
ovoid_definition = ovoidDefinitions.OVOID_1
color='black'
fill=color
width=10

# create the ovoid
#path = dwg.path(d='M 50,200 C 50,150 150,150 200,150 S 350,150 350,200 S 250,250 200,250 S 50,250 50,200')
#dwg.add(path.stroke(color=color,width=width).fill("black"))
#dwg.add(dwg.line(start=(50,200), end=(50,150),stroke='red', stroke_width=3))
#dwg.add(dwg.line(start=(200,150), end=(150,150),stroke='red', stroke_width=3))
#dwg.add(dwg.line(start=(350,200), end=(350,150),stroke='red', stroke_width=3))
#dwg.add(dwg.line(start=(200,250), end=(250,250),stroke='red', stroke_width=3))

ov = ovoid.Ovoid(dwg, center=center, ovoid_definition=ovoid_definition, color=color, width=width, fill=fill)

center = (600,190)

ovoid_definition = {key: value * 0.75 for key, value in ovoidDefinitions.OVOID_1.items()}
color='white'
fill=color
width=5
ov_inner = ovoid.Ovoid(dwg, center=center, ovoid_definition=ovoid_definition, color=color, width=width, fill=fill)


#ov.add_circles(dwg,r=5,fill='green')
#ov.add_tangents(dwg)


# set the variables for the ovoid
center=(200,200)
ovoid_definition = ovoidDefinitions.OVOID_2
color='black'
fill='black'
width=10

ov2 = ovoid.Ovoid(dwg, center=center, ovoid_definition=ovoid_definition, color=color, width=width, fill=fill)
#dwg.add(dwg.circle(center=(center[0],center[1]-25),r=50, fill='red'))
#ov2.add_circles(dwg,r=5,fill='green')
#ov2.add_tangents(dwg)

center=(500,500)
ovoid_definition = ovoidDefinitions.OVOID_3
color='black'
fill='black'
width=10

ov3 = ovoid.Ovoid(dwg, center=center, ovoid_definition=ovoid_definition, color=color, width=width, fill=fill)


# Save the file
dwg.save()

#Display
x=0
y=0
#app = QApplication([]) 
#if True:
#    svgWidget = QSvgWidget(filename)
#else:
#    svgWidget = QSvgWidget(dwg.tostring())
#sizeHint = svgWidget.sizeHint()
#print(sizeHint)
#svgWidget.setGeometry(x,y,1000,1000)#*sizeHint.width(),10*sizeHint.height())
#svgWidget.show()       
#sys.exit(app.exec_())            
