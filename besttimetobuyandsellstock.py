Solution #1 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = prices[0]
        old_profit = 0
        new_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > min_buy: 
                new_profit = prices[i] - min_buy
            else:
                min_buy = prices[i]
            if old_profit < new_profit: 
                old_profit = new_profit 
        return old_profit 

solution #2 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = prices[0]
        old_profit = 0
        new_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > min_buy: 
                new_profit = max(old_profit, prices[i]-min_buy)
                old_profit = new_profit 
            else:
                min_buy = prices[i]
        return new_profit 
    
Solution #3

 class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        loss= prices[0]
        profit = 0
        for i in range(1, len(prices)):
            loss = min(loss, prices[i])
            profit = max(profit, prices[i]-loss)
        return profit
