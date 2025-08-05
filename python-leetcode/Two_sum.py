class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num not in seen:
                seen[num] = i
            else:
                return (seen[target - num] , i)
        
