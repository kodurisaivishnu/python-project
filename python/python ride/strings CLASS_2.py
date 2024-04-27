#a="sai"
#b=25
#c=200
#print('my name is { }, my age is { } and mymarks are { }'.format(a,b,c))



#x=5
#y=10
#print(f'x is {y } and y is { x}')


#a='Rgukt Basar'
#print(a.capitalize())

#a="sai"
#print(a.isdigit())  #True

#a= "My Name Is Koduri sai vishnu"
#print(a.title())

#print(a.upper())

#print(a.swapcase())


#print(a.rindex('sa'))



#a="rgukt basar"
#print(a.count("bas",10,len(a)))

#print(a.replace("rg","ksv"))

#print(a.split(' '))

#print(a.strip())

#print(a.lstrip("rgu"))
#print(a.rstrip("sa"))         #no

#join()
#a=['rgukt','basar','nirmal']
#b='@'
#print(b.join(a))



#a="rajiv gandhi university"
#print(a.partition(' '))

import string
#print(string.ascii_letters)
#print(string.digits)
#1print(string.whitespace)

#print(string.printable)
import base64

Str = "koduri sai vishnu"
Str = base64.b64encode(Str.encode('utf-8',errors = 'strict'))

print ("Encoded String: " , Str)
print(base64.b64decode(Str.decode('utf-8',errors='strict')))

