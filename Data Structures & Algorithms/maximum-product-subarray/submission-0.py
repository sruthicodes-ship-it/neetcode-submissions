class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min = cur_max = 1

        for n in nums:

            if n == 0:
                cur_min = cur_max = 1
            
            temp = n*cur_max
            cur_max = max(n, temp, n*cur_min)
            cur_min = min(n, temp, n*cur_min)
            res = max(res, cur_max)
        
        return res