array=[3,1,3,2,3]
k=6
k_pair=0
left=0
right=len(array)-1
while right>left:
    if (array[left]+array[right])>=k:
        k_pair+=1
        #array.remove(array[i])
        print(array[left],array[right])
        #array.remove(array[length])
        left+=1
        right-=1
    else:
        break
print(k_pair)