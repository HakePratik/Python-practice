candies = list(map(int,input("enter a candies:").strip().split()))
extracandie=int(input("enter extra candie: "))
def gretestkid(Candies):
    result=[]
    for i in range (len(Candies)):
        for j in range (i):
            if candies[j]>candies[i]+extracandie:
                result.append("false")
                break
        else:
            result.append("true")
    return result
print(gretestkid(candies))
