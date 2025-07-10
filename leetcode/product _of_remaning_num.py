nums=[-1,1,0,3,-3]
answer=[]
def product_of_other_element(nums):
    for i in range(len(nums)):
        product=1
        for j in range (len(nums)):
            if i!=j:
                product *= nums[j]
        answer.append(product)
    return answer
print(product_of_other_element(nums))