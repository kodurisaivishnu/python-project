def count(chr):
	u=l=0
	for i in chr:
		if(i>="A" and i<="Z"):
			u=u+1
		elif(i>"a" and i<="z"):
			l=l+1
	print("uc",u)
	print("Lc",l)
chr=input("Enter any char: ")
count(chr)

