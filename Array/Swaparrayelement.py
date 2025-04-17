"""L=[10,20,30,40,50,60,70,80]
n=int(input("enter change no:"))
for i in range(0,len(L)):
    if L[i]==n:
        temp=L[i]
        L[i]=L[i-1]
        L[i-1]=temp
print (L) """

#without temp variable 
L=[10,20,30,40,50,60,70,80]
n=int(input("enter change no:"))
print (L)
for i in range(0,len(L)):
    if L[i]==n:
        L[i-1],L[i]=L[i],L[i-1]
print (L)
