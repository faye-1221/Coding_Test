class Solution(object):
    def isPalindrome(self, s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while(len(strs) > 1):
            if strs.pop() != strs.pop(0):
                return False
        return True