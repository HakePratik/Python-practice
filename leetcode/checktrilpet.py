nums=[1,2,3,4,5]
for i in range(1,len(nums)-1):
    if nums[i-1]<nums[i]<nums[i+1]:
        print('True')
        break
else:
    print('False')
