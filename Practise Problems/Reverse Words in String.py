demo="Welcome to this JavaScript Guide!"

result=""
res=""
for i in range(len(demo)-1,-1,-1):
# for i in demo:
    result +=demo[i]
result=result.split()
for i in range(len(result)-1,-1,-1):
    res+=result[i]+" "
print(res)
