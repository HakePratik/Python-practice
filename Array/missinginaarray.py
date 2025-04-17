"""a=[10,20,30,40,50]
for i in a:
    print (a)
    a.remove(i)
    print (i)
    
print (a)

#single value missing 
a=[1,2,3,4,5,6,7,8,10]
add=0
for i in range(len(a)):
    add+=a[i]
print (55-add)"""

a=[10,2,3,4,5,6,8,1]
a=a.sort()
add=1
for i in range(10):
    if a[i]==add:
        add+=1
    elif add!=a[i]:
        print (add)
    break
print (a)
