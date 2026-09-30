class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def max_amount(i):

            if i >= len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(nums[i]+max_amount(i+2), max_amount(i+1))
            return memo[i]
        
        return max_amount(0)
        