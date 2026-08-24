
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix, suffix = [], []
        value, value1 = 1, 1

        # prefix products
        for i in range(len(nums)):
            prefix.append(value)
            value *= nums[i]

        # suffix products (built in reverse)
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(value1)
            value1 *= nums[i]
        
        suffix.reverse()  # to align suffix with nums order

        # combine prefix and suffix
        result = [prefix[i] * suffix[i] for i in range(len(nums))]
        
        return result
        