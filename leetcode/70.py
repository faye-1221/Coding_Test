# 피보나치 수 문제와 연결해 쉽게 풀이가 가능하다.

# 재귀 구조 브루트 포스: 타임아웃
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
# 메모이제이션
class Solution(object):
    dp = collections.defaultdict(int)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]