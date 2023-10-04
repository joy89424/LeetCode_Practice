class Solution:
    def climbStairs(self, n: int) -> int:
        step_all = []
        step_all.append(0)
        step_all.append(1) # step_all[1] = 1
        step_all.append(2) # step_all[2] = 2
        # 階梯問題 :
        # 從第三層之後，都是從前一層來或是前兩層來，所以將前兩層的答案相加，就能得到這層的方法數
        for i in range(3,46):
            step_all.append(step_all[i-2] + step_all[i-1])
        return step_all[n]