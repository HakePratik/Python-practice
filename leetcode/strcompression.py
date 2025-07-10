char=['a','a','b','a','a','a','a','a','a','a','a','a']
unique=[]
result=[]
for i in char:
    if i not in unique:
        unique.append(i)
for i in unique:
    count=0
    result.append(i)
    for j in range(len(char)):
        if i==char[j]:
           count+=1
    strcount=str(count)
    for i in range(len(strcount)):
        result.append(strcount[i])
print(result)
print("".join(result))