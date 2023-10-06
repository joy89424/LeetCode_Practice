# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 比較左右深度
def depth_hight(root):
    if root != None:
        # 只要左邊或右邊回傳-1，回傳-1跳出遞迴
        l_height = depth_hight(root.left)
        if l_height == -1:
            return -1
        r_height = depth_hight(root.right)
        if r_height == -1:
            return -1
        # 當左邊或右邊深度超過1，就回傳-1跳出遞迴
        if abs(l_height-r_height) >1:
            return -1
        return max(l_height, r_height)+1
    else:
        return 0

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height-balanced 兩邊深度不超過1
        if depth_hight(root) == -1:
            return False
        else:
            return True