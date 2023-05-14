a=int(input())
b=int(input())
if a>b:
    large=a
else:
    large=b
while(True):
    if large%a==0 and large%b==0:
        print(large)
        break
    large=large+1        