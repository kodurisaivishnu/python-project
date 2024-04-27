from turtle import *
pensize('60')
speed(0)
r=30
for i in range(1,500):
	for color in('red','green','white','black'):
		pencolor(color)
		circle(r+i,5)