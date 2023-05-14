r=int(input())
unit=int(input())
n=int(input())
arr=list(map(int,input().split()))
def Funct(r,unit,n,arr):
     if n == 0:
       return -1
     total_sum=r*unit
     sum=0
     count=0
     for i in range(n):
        sum+=arr[i]
        count=count+1
        if sum>=total_sum:
            break
     if total_sum>sum:
            return 0
     return count  
print(Funct(r,unit,n,arr))
