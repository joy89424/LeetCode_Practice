class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        # current = len(nums)-1 時，代表 current 指向 list最後
        while current != len(nums)-1:
            # nums[] 與下一個數字相同時，需移除一個
            if nums[current] == nums[current+1]:
                nums.remove(nums[current])
            else:
                current+=1
        return len(nums)