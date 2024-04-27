
#1

'''name=input("Enter any string:  ")
result=' '
for i in range(len(name)):
	result+=name[i]
print(result)
print(name)'''


#2


'''for i in range(1,6):
	t=65
	for j in range(1,i+1):
		print(chr(t),end='')
		t=t+1
	print()'''
	

#---------->     print(ord('Z'))

#3

while(1):

	name =input("Enter your name: ")
	if ((name.replace(" ",'')).isalpha()==False) :
		print("invalid name")
		break
		
	else:
		pan=input("Enter your pan number: ")
		if(len(pan) !=10 or (pan[0:5]+pan[9:]).isupper()==False or (pan[5:9]).isdigit==False):
			print("invalid pan number")
			break
	print("Dear {},your pan number is {}".format(name,pan))
	break 

			
						
										
			
#16



'''s=input("Enter your string: ")
if(len(s)%4 ==0):
	t=' '
	for i in range(len(s)-1,-1,-1):
		t=t+s[i]
	print(t)
else:
	print(s)'''
	
#---------->  "   ' '.join(reversed(s)) " we can use.


#7




