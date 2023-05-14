n=int(input())
rev=int(0)
while n > 0:
    #rem=n%10
    rev =rev * 10 + n%10
    n=n//10
print('revered no :',rev)  

