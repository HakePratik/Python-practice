
numbers = int(input("Enter a number of elements in array :"))
listM=[]
listdiff=[]
for i in range (0,numbers):
    M=int(input('enter element in array:'))
    listM.append(M)
listM=list(map(int,listM))
print ("list of elements:",listM)
for i in range (len(listM)):
     if i<len(listM)-1:
         D=listM[i+1]-listM[i]
         i+=1
         listdiff.append(D)
print ("difference between elements list:",listdiff)
a=(sum(listdiff)/len(listdiff))
print("Avarage value of difference between element:",a)