# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 用遞迴方式，依序搜尋 左->中間->右邊 是否有節點
def inorder(root, inorder_output):
    if root == None:
        return
    inorder(root.left, inorder_output)
    inorder_output.append(root.val)
    inorder(root.right, inorder_output)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_output = []
        inorder(root,inorder_output)
        return inorder_output