n=int(input())
def check(n):
    temp=n
    sum=0
    while n!=0:
        k = n % 10
        sum = sum + k
        n = n // 10
    if temp % sum == 0:
        print("Yes Divisible")
    else:
        print("Not Divisible")  
check(n)          
         
