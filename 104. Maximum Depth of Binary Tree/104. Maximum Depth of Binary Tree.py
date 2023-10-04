# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def Max_depth(root):
    #         3(3)
    #       /     \
    #    9(1)     20(2)
    #            /    \
    #          15(1)  7(1)
    if root is not None:
        left_depth = Max_depth(root.left)
        right_depth = Max_depth(root.right)
        return max(left_depth, right_depth) + 1
    else:
        return 0
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return Max_depth(root)