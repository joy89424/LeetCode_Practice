class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        # 當不一樣的時候，就直接往前覆蓋前面的數字，並且將count+1
        #    [1,1,2,3] count=1  |  1跟1一樣，所以不動
        # -> [1,1,2,3] count=1  |  1跟2不一樣，所以將nums[count]覆蓋為2
        # -> [1,2,2,3] count=2  |  2跟3不一樣，所以將nums[count]覆蓋為3
        # -> [1,2,3,3] count=2  |  2跟3不一樣，所以將nums[count]覆蓋為3
        # 最後再return nums的前count個數字
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[count] = nums[i+1]
                count+=1
        return count