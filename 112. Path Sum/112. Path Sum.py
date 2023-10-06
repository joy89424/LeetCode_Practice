# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sub_val(root, targetSum):
        if root != None:
            targetSum = targetSum - root.val
            print("targetSum", targetSum)
            if targetSum is 0 and root.left is None and root.right is None:
                return True
            else:
                left_has_path = sub_val(root.left, targetSum)
                right_has_path = sub_val(root.right, targetSum)
                return left_has_path or right_has_path # 只要任何一邊回傳true，最後皆是回傳true
        else:
            return False
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return sub_val(root, targetSum)