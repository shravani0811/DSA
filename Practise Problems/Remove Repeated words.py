a="the quick brown fox went after the other fox for a quick meal"

# demo="Welcome to this JavaScript Guide!"

res=[]
temp={}
a=a.split()

# for i in a:
#     if i not in res:
#         res.append(i)
#     else:
#         res.remove(i)
            
# print(res)

for i in a:
    if i not in temp:
        temp[i]=1
    else:
        temp[i]+=1
for key, val in temp.items():
    if val==1:
        res.append(key)
print(res)