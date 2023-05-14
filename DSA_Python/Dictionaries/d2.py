dic={0:[{2:"a"},4,"d"],1:"b"}
print(type(dic))
print(dic)
print(dic.values())
print(dic[0])
for k,v in dic.items():
    print(k,v)
for i in enumerate(dic.items()):
    print(i)    
print(sorted(dic))    
print(dic)
print(dic[0][1])