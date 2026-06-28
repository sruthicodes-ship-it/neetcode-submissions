class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        stack = []
        for i in operations:
            if i == "+":
                val = stack[-1]+stack[-2]
                stack.append(val)
                sum += val
            elif i == "D":
                val = 2*stack[-1]
                stack.append(val)
                sum += val
            elif i == "C":
                val  = stack.pop()
                sum -= val
            else:
                val = int(i)
                stack.append(val)
                sum += val
        
        return sum
