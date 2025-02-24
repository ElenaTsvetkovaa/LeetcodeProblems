# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node(self, head):
        head.next = head.val



head = [1,2,3,4,5,6]
print(Solution().middle_node(head))

