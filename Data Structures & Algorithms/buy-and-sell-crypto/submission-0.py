class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = float('inf')
        profit = 0
        for i in prices:
            if i < buying_price:
                buying_price = i
            value = i - buying_price
            if value > profit:
                profit = value
        
        return profit