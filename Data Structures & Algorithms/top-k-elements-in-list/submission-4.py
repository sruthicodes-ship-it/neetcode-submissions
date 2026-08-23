class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums = {}
        output = []

        # Count frequency
        for num in nums:
            countnums[num] = countnums.get(num, 0) + 1

        # Find the most frequent k elements
        for i in range(k):
            max_num = max(countnums, key=countnums.get)

            output.append(max_num)

            del countnums[max_num]

        return output