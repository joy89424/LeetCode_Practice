class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 要注意不能更改nums1的長度，不然會報錯或塞不進去
        if n == 0:
            nums2 = []
        for i in range(len(nums2)):
            nums1[m+i] = nums2[i]
        nums1.sort()
        print(nums1)