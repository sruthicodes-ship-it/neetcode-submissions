class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for key,value in enumerate(nums):
            if key>0 and value == nums[key-1]:
                continue
            l,r = key+1, len(nums)-1
            while l<r:
                threesum = value+nums[l]+nums[r]
                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l +=1
                else:
                    res.append([value, nums[l],nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        
        return res
        