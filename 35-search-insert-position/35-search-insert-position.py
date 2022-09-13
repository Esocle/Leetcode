class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] == target:
                index = i
            else:
                if nums[i-1] < target and nums[i] > target:
                    index = i
        if index == 0: 
            if target > nums[-1]: index = len(nums)
        return index