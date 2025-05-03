# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = deque([(p, q)])

        while queue:
            p, q = queue.popleft()

            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(None)
q.right = TreeNode(3)

print(Solution().isSameTree(p,q))