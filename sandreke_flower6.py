from turtle import *
from colorsys imprt *

bgcolor( 'black' )
tracer(2)
pensize(2)
h=0

for i in range(180):
c = hsv_to_rgb(h,1,1)
h += 0.005
color(c)
up(), goto(-8,25), down(), forwar(i)
rigth(89), fillicolor(c), begin_fill()
circle(90,100), end_fill(), left(179)
back(i,2), left(6)

done()
