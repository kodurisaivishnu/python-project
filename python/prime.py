n=int(input("Enter the Range: "))
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        print(i)