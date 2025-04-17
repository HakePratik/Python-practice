L=[10,20,30,40,50,20,60,70,80,]
number= int(input("enter a number:"))
occurrence= 0
for i in range(0, len(L)):
        if L[i]==number:
                occurrence+=1
print (occurrence)