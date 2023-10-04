class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=[]
        for i in range(len(prices)):
            for j in range (1, len(prices)):
                if j>i and prices[j]<=prices[i]:
                    res.append(prices[i]-prices[j])
                    break
            else:
                    res.append(prices[i])
        return res