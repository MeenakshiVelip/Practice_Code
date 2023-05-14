n1= input()
n2= input()
n3= input()

vowel="AEIOUaeiou"
cons="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
for i in vowel:
   n1= n1.replace(i,"#")
for i in cons:
   n2= n2.replace(i,"%")
ans=n1+n2+n3.upper()   
print(ans)            