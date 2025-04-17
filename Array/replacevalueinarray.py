L=[10,20,30,40,50,60]
change_n=int(input("enter change the number:"))
true=0
for i in range(len(L)):
    if L[i] ==change_n:
        replace_n=int(input("enter replacement number:"))
        L[i] = replace_n
        true=1
if true==0:
        print ("Number is not present in array!!")
print ("array is :",L)