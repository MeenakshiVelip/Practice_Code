n=int(input())
temp=1
if (n<=100):
    while temp<=n:
        n=n^temp
        temp=temp<<1
    print(n)    
else:
    print("Wrong Output")        


