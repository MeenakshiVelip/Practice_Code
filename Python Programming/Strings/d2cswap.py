n=int(input())
a=input()
b=input()
c=input()
flag=1
for i in range(len(a)):
    if a[i]!=c[i] and b[i]!=c[i]:
        flag=0
        #break
if flag==1:
    print("yes")
else:
    print("no")            
   
 