def search(arry,n,x):
    for i in range(0,n):
        if (arry[i]==x):
            return i
    return -1
arry=[1,5,7,8,57,6]
x=int(input("enter"))
n=len(arry)
result=search(arry,n,x)
if result==-1:
    print("not prasent")
else:
    print ("prasent", result,x)
