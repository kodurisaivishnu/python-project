'''d={}
d[1]=100
d['x']='rgukt'
print(d[1])
print(d['x'])'''


#2

'''d={1:5,5:20,7:100}
print(d.get(1))
print(d[1])'''


#3

#d={1:2,3:4,5:6,7:8}
#print(4 in d)
'''x=d.items()
print(x)'''

'''for i,j in d.items():
	print(i,j)'''
	
	
#4

'''d={1:5,'a':10,3:20}
x=d.keys()
print(x)
for i in x:
	print(d[i])'''
#also we have values()


#5

####                 

                 
                              # d={1:5,'x':100,6:55}
                              
                              
                              
'''for i in list(d.keys()):
	d.pop(i)
	
print(d)'''


#6

'''d.popitem()
print(d)'''

#check print(d.popitem()) observe difference..

#7 

'''for i in range(len(d)):
	d.popitem()
print(d)'''

#8

'''l=[1,5,10,'x']
d=dict.fromkeys(l)
d[5]=10
print(d)'''

#9
'''x=d.copy()
print(x)'''

#10


'''d1={1:2,3:4}
d2={4:5,5:6,7:8}
print(d1)
print(d2)
d2.update(d1)
print(d2)'''


