#copyrights by koduri sai vishnu
print('CAUTION : THIS CODE IS COPYRIGHTED BY KODURI SAI VISHNU')
print( )
print( )

a= [1,4,4,0,2,5,0,3,6,1,4,6]
b=[1,2,3,4,5,6,7,8,9,10,11,12]
z=dict(zip(b,a))
a,b,g=input("ENTER YOUR DATE OF BIRTH : [ DD/MM/YYYY ] : ").split('/')
y=int(a)
c=int(b)
d=int(g)

print( )
for x in z:
	if(x==c):
		i=z[c]
if(d>=2000):
	k=6
else:
	k=0
o=d%100
j=o//4
g=y+i+k+o+j
f=g%7

my_dict={0:'SATURDAY',1:'SUNDAY',2:'MONDAY',3:'TUESDAY',4:'WEDNESDAY',5:'THURSDAY',6:'FRYDAY'}
print( 'YOU BORN ON ' ,'"',my_dict[f],'"')