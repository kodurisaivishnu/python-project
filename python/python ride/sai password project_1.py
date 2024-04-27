from random import *
x=input("your pass:   ")
a="kodurisaivishnu"
b="123456789"
c="%©$€€¢¢^={{"
for i in range(40000):
	t=a+b+c
	length=8
	password="".join(sample(t,length))
	while(x!=password):
		print(password)
		break
		print(password)