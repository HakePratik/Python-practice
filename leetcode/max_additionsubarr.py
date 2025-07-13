nums = [1, 12, -5, -6, 50, 3]
k = 4

class Solution(object):
   
    def findMaxAverage(nums, k):
        maxi = float('-inf')
        for i in range(len(nums) - k + 1):
            add = 0
            for j in range(i, i + k):
                add += nums[j]
            print(add)
            maxi = max(add, maxi)
        return maxi / k

print(Solution.findMaxAverage(nums, k))


