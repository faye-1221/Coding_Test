# heapq 모듈 이용
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(1, k):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)

# heapq 모듈의 heapify 이용
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heapq.heapify(nums)
        
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

# heapq 모듈의 nlargest 이용
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return heapq.nlargest(k, nums)[-1]
    
# 정렬을 이용한 풀이
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return sorted(nums, reverse=True)[k-1]