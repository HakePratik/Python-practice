n=int (input("Enter a number for additional of the two elements:"))
L=list(map(int,input("enter a array element:").split()))
for i in range(0, len(L)):
     for j in range (i+1,len(L)):
             if ((L[i]+L[j])==n):
                L1=[]
                L1.append(L[i])
                L1.append(L[j])
                print (L1)