l=int(input('enter the A row size: '))
m=int(input('enter the A column size: '))
x=int(input('enter the B row size: '))
y=int(input('enter the B column size: '))

if (m==x):
    
    A=[]
    for i in range(l):
        C=[]
        for j in range(m):
            C.append(int(input("Enter elements of A: ")))
        A.append(C)
         
    B=[]
    for i in range(x):
         C=[]
         for j in range(y):
             C.append(int(input("Enter the B value:     ")))
         B.append(C)
    
    R=[]
    for i in range(l):
        C=[]
        for j in range(y):
            C.append(0)
        R.append(C)
    
    for i in range(l):
        for j in range(y):
            for k in range(x):
                R[i][j]=R[i][j]+A[i][k]*B[k][j]
    print()
    print(R)
else:
    print()
    print("Matrix multiplycation not possible..")