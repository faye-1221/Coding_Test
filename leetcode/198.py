# 재귀 구조 브루트 포스: 타임아웃
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_(i):
            if i < 0:
                return 0
            return max(rob_(i-1), rob_(i-2) + nums[i])
        
        return rob_(len(nums)-1)

# 타뷸레이션
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp.popitem()[1]