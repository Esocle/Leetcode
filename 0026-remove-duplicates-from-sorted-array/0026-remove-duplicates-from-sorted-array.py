class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums))
        temp.sort()
        for i, e in enumerate(temp):
            nums[i] = e
            
        return len(temp)