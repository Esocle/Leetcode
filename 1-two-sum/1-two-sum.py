class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = target - nums[i]
            try:
                if i != nums.index(temp):
                    return [i, nums.index(temp)]                  
            except:
                continue