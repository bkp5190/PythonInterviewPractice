from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertBinaryTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Recursive DFS
    if not root:
        return None

    # Swap the children
    temp = root.right
    root.right = root.left
    root.left = temp

    # Recursive calls
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

    return root
