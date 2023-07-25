class Solution(object):
    def combine(self, n, k):
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return results

class Solution(object):
    def combine(self, n, k):
        return list(itertools.combinations(range(1, n+1), k))