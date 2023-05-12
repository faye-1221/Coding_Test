class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        n = 1
        for i in range(0, len(nums)):
            answer.append(n)
            n = n * nums[i]
        n = 1
        for i in range(len(nums)-1, 0-1, -1):
            answer[i] = answer[i] * n
            n = n * nums[i]
        return answer