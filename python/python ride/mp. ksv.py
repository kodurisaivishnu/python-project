from turtle import *
def msg( ):
	x=x**2
speed(0)
fd(500)
rt(180)
fd(1000)
rt(180)
fd(500)
lt(90)
fd(1000)
rt(180)
fd(2000)
penup( )
goto(490,-25)
write('>')
goto(-500,-25)
write('<')
goto(-8,970)
write('^')
goto(0,0)
write('0')
lt(90)
for i in range(1,10):
	fd(50)
	write(i)
	goto(0,0)
for i in range(1,10):
	fd(50)
	rt(0)
	write(i)
	