def main():
  def checkp(n):
    sum1,sum2 = 0,0
    for i in range(len(n)):
       if i % 2 == 0:
          sum1+=ord(n[i])
       else:
          sum2+=ord(n[i])
    ans=abs(sum2-sum1)
    if (ans%3==0 or ans%5==0 or ans%7==0):
      print("Prime String")
    else:
      print("Casual String")
  t=int(input())
  n=[]
  ind=[]
  for i in range(0,t):
    n.append(input())
  for i in n:
    ind.append(n.index(i)) 
  for  i in ind: 
    checkp(n[i])  
main()          
    
            
