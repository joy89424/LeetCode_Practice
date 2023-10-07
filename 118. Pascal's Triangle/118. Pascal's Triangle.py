class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            # 大於2之後，前兩層必為[[1],[1,1]]
            Ans = [[1],[1,1]]
            for i in range(2, numRows):
                # 頭=1
                level = [1]
                # 每一層總共需要執行 n-2次 ，又因為 n=i+1，所以 n-2 = (i+1)-2 = i-1 次
                for j in range(i-1):
                    level.append(Ans[i-1][j]+Ans[i-1][j+1]) # 前一層的數字依序取兩個相加
                # 尾=1
                level.append(1) 
                Ans.append(level)
            return Ans
