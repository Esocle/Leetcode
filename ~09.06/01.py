class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(len(nums)):
                if temp == nums[j]:
                    if i != j:
                        return [i, j]

a = Solution()
result = a.fourSum([1,0,-1,0,-2,2], 0)
print(result)