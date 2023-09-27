class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        dic = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in dic:
                stack.append(char)
            elif not stack or dic[char] != stack.pop():
                return False
        
        return len(stack) == 0