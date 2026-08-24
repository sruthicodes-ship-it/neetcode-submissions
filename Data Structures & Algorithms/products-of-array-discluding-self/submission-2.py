class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, result = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        value, value1 = 1, 1

        for i in range(len(nums)):
            if i>0:
                value = value* nums[i-1]

            prefix[i] = value

        for i in range(len(nums) - 1, -1, -1):
            if i< (len(nums)-1):
                value1 = value1* nums[i+1]
            suffix[i] = value1

        for i in range(len(nums)):
            result[i] = prefix[i]*suffix[i]
        
        return result