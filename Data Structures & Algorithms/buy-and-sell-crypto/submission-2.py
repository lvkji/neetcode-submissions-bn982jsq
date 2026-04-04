class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        while right != len(prices):
            #If profit can be made compute and replace
            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]
                maxProfit = max(profit,maxProfit)
                right+=1
            #Either no profit or los ==> Slide Window
            elif prices[left] >= prices[right]:
                left = right
                right+=1
        return maxProfit
