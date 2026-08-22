class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracknums = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in tracknums:
                return [tracknums[value], i]
            
            tracknums[nums[i]] = i
        
        return []