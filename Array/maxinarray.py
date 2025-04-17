L=[10,20,30,40,50,60,70,80]
max=L[0]
for i in range(1,len(L)):
    if max<L[i]:
        max=L[i]
print ("  ",max)