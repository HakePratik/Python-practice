L=[10,20,30,40,50,60,70,80,10,80]
for i in range(0, len(L)):
     for j in range (i+1,len(L)):
         if L[i]==L[j]:
                print (L[j])