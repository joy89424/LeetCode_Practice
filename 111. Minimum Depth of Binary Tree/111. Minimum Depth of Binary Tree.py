# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def deep(root):
    if root != None:
        l_depth = deep(root.left)
        r_depth = deep(root.right)
        if l_depth and r_depth:
            return min(l_depth, r_depth) + 1
        elif l_depth:
            return l_depth + 1
        elif r_depth:
            return r_depth + 1
        else:
            return 1
    else:
        return 0
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return deep(root)