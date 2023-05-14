n=int(input())
while n==0:
    n=n-1 
    a=input()
    b=input()
    c=input()
    flag=1
    for i in range(len(a)):
      if a[i]==c[i] or b[i]==c[i]:
         break
      flag=0     
if flag==1:
    print("yes")
else:
    print("no")            
   
 