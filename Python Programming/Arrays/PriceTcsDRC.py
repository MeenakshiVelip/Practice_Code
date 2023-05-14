itemno =[101,102,103,104]
itemname=['milk','cheese','ghee','bread']
price=[42,50,500,40]
stock=[10,20,15,16]
n=int(input())
q=int(input())
if n in itemno:
   index1=itemno.index(n)
   if q<=stock[index1]:
     print(f"{float(q*price[index1])}")
     stock[index1]=stock[index1]-q
     print(f"{stock[index1]}  LEFT")
   else:
     print("No Stock")
     print(f"{stock[index1]}  LEFT")
else:
   print("INVALID INPUT")       

        
     