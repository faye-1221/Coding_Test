# 내  풀이: 시간 초과
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """

#         best = 0

#         for idx, p in enumerate(prices):
#             for idx2 in range(idx+1, len(prices)):
#                 p2 = prices[idx2]
#                 if (p < p2) and (best < p2-p):
#                     best = p2-p
#         return best

# 브루트 포스 계산(책 예시)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_price = 0
        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        return max_price
    
# 지점과 현재 값과의 차이 계산
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price- min_price)
        
        return profit