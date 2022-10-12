class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        for i in range(n-3, -1, -1):
            if nums[i]+nums[i+1]<=nums[i+2]: continue
            answer = nums[i] + nums[i+1] + nums[i+2]
            break
        
        return answer