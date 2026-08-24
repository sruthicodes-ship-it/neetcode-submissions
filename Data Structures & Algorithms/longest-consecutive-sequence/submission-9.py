class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)
        for n in nums:
            if n-1 not in numsSet:
                streak = 0
                while n+streak in numsSet:
                    streak += 1
                res = max(res, streak)
        
        return res