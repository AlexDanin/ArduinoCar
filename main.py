import sys
import dxfgrabber as dg
import turtle as tut

from numpy import pi,cos,sin,arctan2,sqrt

fname="qwerty4.dxf"
dxf=dg.readfile(fname)
print(dxf.header)

def tut_dxfline(l):
    x0=l.start[0]
    y0=l.start[1]
    x1=l.end[0]
    y1=l.end[1]
    deg = arctan2(y1-y0,x1-x0) / pi*180
    dist = sqrt((x1-x0)**2+(y1-y0)**2)

    tut.penup()
    tut.setpos(x0,y0)
    tut.setheading(deg)
    tut.pendown()
    tut.forward(dist)




tut.speed("fastest")


for entity in dxf.entities:
    if entity.dxftype == 'LINE':
        tut_dxfline(entity)
    else:
        print(entity.dxftype)

print("Draw End")            
tut.mainloop()