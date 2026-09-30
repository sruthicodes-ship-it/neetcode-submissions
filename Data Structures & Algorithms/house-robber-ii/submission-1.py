class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1]*2 for i in range(len(nums))]

        def max_amount(i, Flag):

            if i >= len(nums) or (Flag and i == len(nums)-1):
                return 0
            
            if memo[i][Flag] != -1:
                return memo[i][Flag]
            
           
            memo[i][Flag] = max(nums[i]+max_amount(i+2, Flag), max_amount(i+1, Flag))
            
            return memo[i][Flag]
        
        return max(max_amount(0, True), max_amount(1, False))