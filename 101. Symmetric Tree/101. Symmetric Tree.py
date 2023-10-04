# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder_l(root, left_list):
    if root != None:
        left_list.append(root.val) # 將所有路徑記錄下來
        inorder_l(root.left, left_list)
        inorder_l(root.right, left_list)
    else:
        left_list.append(None)

def inorder_r(root, right_list):
    if root != None:
        right_list.append(root.val) # 將所有路徑記錄下來
        inorder_r(root.right, right_list)
        inorder_r(root.left, right_list)
    else:
        right_list.append(None)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 一個使用左搜尋，另一個使用右搜尋
        # 結果一樣時，就是結果
        left_list = []
        right_list = []
        inorder_l(root, left_list)
        inorder_r(root, right_list)
        if left_list == right_list:
            return True
        else:
            return False