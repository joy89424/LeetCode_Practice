# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def find_root(list1, root):
    if list1 == []:
        return
    # 找出root的左邊list跟右邊list
    if len(list1) % 2 == 0:
        l_list = list1[:int(len(list1) / 2)]
        r_list = list1[int(len(list1) / 2):]
    else:
        l_list = list1[:int((len(list1) + 1) / 2)]
        r_list = list1[int((len(list1) + 1) / 2):]

    # 找出root的左邊節點
    if len(l_list) % 2 == 0:
        root.left = TreeNode(l_list[int(len(l_list) / 2)])
        l_list.pop(int(len(l_list) / 2))
        find_root(l_list, root.left)
    else:
        root.left = TreeNode(l_list[int((len(l_list) - 1) / 2)])
        l_list.pop(int((len(l_list) - 1) / 2))
        find_root(l_list, root.left)

    if r_list == []:
        return
    # 找出root的右邊節點
    if len(r_list) % 2 == 0:
        root.right = TreeNode(r_list[int(len(r_list) / 2)])
        r_list.pop(int(len(r_list) / 2))
        find_root(r_list, root.right)
    else:
        root.right = TreeNode(r_list[int((len(r_list) - 1) / 2)])
        r_list.pop(int((len(r_list) - 1) / 2))
        find_root(r_list, root.right)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 抓最中間的值，也就是抓出root
        if len(nums) % 2 == 0:
            root = TreeNode(nums[int(len(nums) / 2)])
            nums.pop(int(len(nums) / 2))
        else:
            root = TreeNode(nums[int((len(nums) - 1) / 2)])
            nums.pop(int((len(nums) - 1) / 2))

        # 分出左邊跟右邊的list -> 抓出左邊root-> 抓出右邊root
        find_root(nums, root)
        return root