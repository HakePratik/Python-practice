def sort(arr):
 n=len(arr)
 for i in range (n):
     for j in range (i+1,n):
         if arr[j]<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
arr=[1,45,23,44,5,98]
sort(arr)
print (arr)