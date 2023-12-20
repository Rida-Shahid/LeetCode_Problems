class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sum_chocolates = prices[0] + prices[1]
        if sum_chocolates > money:
            return money
        else:
            return money- sum_chocolates
        