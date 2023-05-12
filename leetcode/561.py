class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 오름차순 풀이
        # pair = []
        # result = 0
        # nums.sort()

        # for n in nums:
        #     pair.append(n)
        #     if len(pair) == 2:
        #         result += min(pair)
        #         pair = []
        # return result


        # 짝수 번째 계산
        # result = 0
        # nums.sort()

        # for idx, n in enumerate(nums):
        #     if idx % 2 == 0:
        #         result += n
        # return result


        # 파이썬다운 방식
        return sum(sorted(nums)[::2])