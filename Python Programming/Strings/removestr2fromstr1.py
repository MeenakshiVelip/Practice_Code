str1=input()
str2=input()
while str2 in str1:
    str1=str1.replace(str2,'')
print(str1)    