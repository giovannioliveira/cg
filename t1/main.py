from turtle import *
from math import pi,sin,cos,acos,degrees,sqrt

def f(theta):
    return 100*theta

domain = [0,2*pi]
npts = 100
size = 10
margin = 10

setworldcoordinates(min-margin,min-margin,max+margin,max+margin)
ht()

dlen = domain[1]-domain[0]
dtheta = dlen/npts

theta = 0
mag = f(theta)
x = mag*cos(theta)
y = mag*sin(theta)
forward(x)
left(90)
forward(y)
right(90)

for i in range(1,npts+1):

    theta2 = theta + dtheta
    mag2 = f(theta2)
    x2 = mag2 * cos(theta2)
    y2 = mag2 * sin(theta2)

    r = sqrt((x2-x)**2+(y2-y)**2)
    dt = acos((x2-x)/r)
    if(y2<y):
        dt*=-1
    left(degrees(dt))
    forward(r)
    right(degrees(dt))

    theta = theta2
    mag = mag2
    x = x2
    y = y2

    if(abs(x)>size):
        setworldcoordinates(min, min, max, max)
        if(x>max):
            max=x
        elif(x<min):
            min = x
        if(y>max):
            max=y
        elif(y<min):
            min=y


done()