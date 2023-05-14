n=int(input("enter number of rows"))
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
     #display spaces   
        print(" ",end="")
    #dislpay *
    for k in range(1,i+1):
        print("*",end="")
    print() 