n=list(map(int,input("enter hour list work in days:"). split ()))
grether = 0
lesser = 0
consist =[ ]
for i in range (len(n)):
    if n[i]>6:
        grether+=1
        if i==(len(n)-1):
            consist.append(grether)
    elif n[i]<6:
        consist.append(grether)
        grether=0
print (consist)
print (max(consist))