class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map =  {}
        for i, n in enumerate(nums):
            nums_map[n] = i

        for i, n in enumerate(nums):
            if (target- n in nums_map) and i != (nums_map[target-n]):
                return [i, nums_map[target-n]]