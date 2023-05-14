s=input()
while len(s)!=0:
        s=s.replace('()', '')
        s=s.replace('[]', '')
        s=s.replace('{}', '')
if len(s)==0:
    print('Balanced')
else:
    print("unbalanced")
        


          