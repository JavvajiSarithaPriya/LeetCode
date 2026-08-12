class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini=prices[0]
        maxi=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            profit=prices[i]-mini
            maxi=max(maxi,profit)
        return maxi
