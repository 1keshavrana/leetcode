class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        re = nums[0]
        maxEnding = nums[0]

        for i in range(1, len(nums)):
        
            maxEnding = max(maxEnding + nums[i], nums[i])
            re = max(re, maxEnding)
    
        return re