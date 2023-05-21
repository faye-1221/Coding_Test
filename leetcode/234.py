# 리스트 변환
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = []
        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while(len(q) > 1):
            if q.pop(0) != q.pop():
                return False
        
        return True
    
# deque
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = collections.deque()

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while(len(q) > 1):
            if q.popleft() != q.pop():
                return False
        
        return True

# 런너를 이용한 풀이★
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev