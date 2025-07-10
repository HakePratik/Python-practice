str1='Tcs'
str2='Google'
def stralt(str1,str2):
    i=j=0
    result=[]
    while i<len(str1) or j<len(str2):
        if i<len(str1):
            result.append(str1[i])
            i+=1
        if j<len(str2):
            result.append(str2[j])
            j+=1
    return ''.join(result)
print(stralt(str1,str2))