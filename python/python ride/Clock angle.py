print()
print("	CAUTION: THIS CODE IS COPYRIGHTED KODURI SAI VISHNU")
import time
print()
print()
x,y=input("		ENTER THE TIME (eg: 5:06):  ").split(":")
print()
print("		PLEASE WAIT.........")
print()
time.sleep(0.5)
print(		"		ALMOST DONE....")
time.sleep(0.5)
h=int(x)
m=int(y)
c=(30*h)-(5.5*m)
print()
print()
print(f"		ANGLE BETWEEN THE HANDS IS {c}°")