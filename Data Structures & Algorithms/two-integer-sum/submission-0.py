class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracknums = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if nums[i] in tracknums:
                return [tracknums[nums[i]], i]
            
            tracknums[value] = i
        
        return []