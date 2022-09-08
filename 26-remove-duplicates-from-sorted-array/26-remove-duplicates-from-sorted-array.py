class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list(set(nums))
        temp.sort()
        for i, e in enumerate(temp):
            nums[i] = e
            
        return len(temp)