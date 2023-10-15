def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1) 

def TraiZero(n):
    count=0
    i=5
    while (n//i != 0):
        count = count+int(n/i)
        i=i*5
    return count    

n=int(input("enter the number"))   
print(fact(n)) 
print(TraiZero(n))      