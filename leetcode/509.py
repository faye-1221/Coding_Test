# 풀이1. 재귀 구조 브루트 포스
class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1)+ self.fib(n-2)

# 풀이2. 메모이제이션(하향식)
class Solution(object):
    dp = collections.defaultdict(int)
    def fib(self, n):
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]

# 풀이3. 타뷸레이션(상향식)
class Solution(object):
    dp = collections.defaultdict(int)
    def fib(self, n):
        self.dp[0] = 0
        self.dp[1] = 1
        
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]

# 풀이4. 두 변수만 이용해서 공간 절약!
# 공간 복잡도가 O(n)에서 O(1)로 줄어든다.
# 시간 복잡도는 동일한 O(n)이라 더 효율적이다.
class Solution(object):
    dp = collections.defaultdict(int)
    def fib(self, n):
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        return x

# 풀이5. 행렬
# O(log n)번의 연산으로 풀 수 있고, 다이나믹 프로그래밍과는 관련 없다.
# 선형대수 관점에서 행렬의 n승을 계산하는 방식으로, numpy 모듈 사용, 리트코드에서는 동작 하지 않음
def fib(n):
    M = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])

    return np.matmul(M ** n, vec)[0]