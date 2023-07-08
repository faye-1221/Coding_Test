class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = []
        l.append(nums[0])
        for i in range(1, len(nums)):
            if l[i-1] > 0:
                l.append(l[i-1] + nums[i])
            else:
                l.append(nums[i])
        return max(l)
    
# 책(메모이제이션): 배열을 nums 그대로 사용하고, if else를 한 줄로 했다는 점이 다름.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        print(nums)
        return max(nums)

# 카데인 알고리즘
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        best_sum = - sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum