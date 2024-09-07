from typing import Optional


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(
            self, root: Optional[TreeNode],
            target: int
    ) -> Optional[TreeNode]:
        if not root:
            return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.val != target:
            return root
        if root.left is None and root.right is None:
            return None
        return root
