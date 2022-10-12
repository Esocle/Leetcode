class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            try:
                if i != nums.index(temp):
                    return [i, nums.index(temp)]                  
            except:
                continue