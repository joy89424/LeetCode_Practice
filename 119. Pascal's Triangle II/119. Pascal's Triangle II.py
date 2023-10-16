class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out_list = [[1], [1, 1]]
        if rowIndex > 1:
            for i in range(rowIndex-1): # 執行n-1次
                level = [1] # 頭=1
                for j in range(i+1): # 中間執行上一行的前兩個相加
                    level.append(out_list[-1][j] + out_list[-1][j+1])
                level.append(1) # 尾=1
                out_list.append(level)
        return out_list[rowIndex]