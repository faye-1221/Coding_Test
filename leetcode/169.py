# 브루트 포스: 시간 초과
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

# 다이나믹 프로그래밍
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums)//2:
                return num

# 분할 정복
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return None
        
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2

        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

# 파이썬 방식
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return sorted(nums)[len(nums)//2]