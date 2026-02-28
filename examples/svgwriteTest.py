#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:40:10 2022

@author: christopherhunter
"""
import sys
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication#, QWidget

import svgwrite
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from svgpython import ovoid



filename = 'svgs/svgwrite-example.svg'
dwg = svgwrite.Drawing(filename)#, size=('100%', '100%'), profile='full')
# draw a red box
#dwg.add(dwg.rect( (10, 10), (30, 20),
#    stroke=svgwrite.rgb(10, 10, 16, '%'),
#    fill='blue') )

#p = svgwrite.path.Path(d="M 10 10", pathLength=10)

#dwg.add(p.stroke(color='blue').fill("red"))
#path = dwg.path(d='M 0,28 H 3 v 1 L 6,27 3,24 v 1 H 0 Z')
#path = dwg.path(d='M 5,25 c 0,5 20,5 15,5')
#dwg.add(path.stroke(color='blue',width=0.2).fill("none"))

#path = dwg.path(d='M 5,25 c 0,-5 20,-5 15,-5')
#dwg.add(path.stroke(color='red',width=0.2).fill("none"))

#path = dwg.path(d='M 20,30 c 5,0 15,0 15,-5')
#dwg.add(path.stroke(color='green',width=0.2).fill("none"))

#path = dwg.path(d='M 20,20 c 5,0 15,0 15,5')
#dwg.add(path.stroke(color='yellow',width=0.2).fill("none"))

dwg.add(dwg.circle(center=(50,500),r=1, fill='red'))
dwg.add(dwg.circle(center=(200,550),r=1, fill='red'))
dwg.add(dwg.circle(center=(350,500),r=1, fill='red'))
dwg.add(dwg.circle(center=(200,450),r=1, fill='red'))
        
center_x=200
center_y=500
length = 150
top_height = 50 
bottom_height = 50
top_scale = .1
bottom_scale = 2
side_scale = 5
color='blue'
width=5
ov = ovoid.Ovoid(dwg, center_x=center_x, center_y=center_y, length=length, top_height=top_height, bottom_height=bottom_height, top_scale=top_scale, bottom_scale=bottom_scale, side_scale=side_scale, color=color, width=width)

#path = dwg.path(d='M 50,500 c 0,5 155,50 150,50 s 150,0 150,-50 s -200,-50 -150,-50 s -150,0 -150,50')
#dwg.add(path.stroke(color='blue',width=0.2).fill("none"))

dwg.add(dwg.circle(center=(50,600),r=1, fill='blue'))
dwg.add(dwg.circle(center=(200,650),r=1, fill='blue'))
dwg.add(dwg.circle(center=(350,600),r=1, fill='blue'))
dwg.add(dwg.circle(center=(200,650),r=1, fill='blue'))
tan1_length=60
tan2_length = 50
path_text = 'M 50,600 C 50,{} {},650 200,650'.format(600+tan1_length,200-tan2_length)
print(path_text)
path = dwg.path(d=path_text)
dwg.add(path.stroke(color='red',width=5).fill("none"))




# Save the file
dwg.save()

#Display
x=0
y=0
app = QApplication([]) 
if True:
    svgWidget = QSvgWidget(filename)
else:
    svgWidget = QSvgWidget(dwg.tostring())
sizeHint = svgWidget.sizeHint()
#print(sizeHint)
svgWidget.setGeometry(x,y,1000,1000)#*sizeHint.width(),10*sizeHint.height())
svgWidget.show()       
#sys.exit(app.exec_())            
