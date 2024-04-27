from turtle import*
import colorsys

speed(0)
h=0.1

def dr():
	global h
	c=colorsys.hsv_to_rgb(h,1,1)
	h+=0.005
	fillcolor(c)
	begin_fill()
	for i in range(8):
		fd(180)
		lt(90)
	end_fill()
		
for j in range(30):
		dr()
		goto(0,0)
		lt(-15)
			
done()
			