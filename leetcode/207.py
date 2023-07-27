# DFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()

        def dfs(i):
            if i in traced:
                return False
            
            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
    
# +) 가지치기로 최적화
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            
            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True