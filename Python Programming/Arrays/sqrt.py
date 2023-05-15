import math
x=int(input("enter x"))
n=x
if x<2:
    print(x)
for i in range(int(math.log(n,2))+1):
    n=(n+(x/n))/2
print(int(n))