class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while 1:
            if i*i == x:
                return i
            elif i*i > x:
                break
            i+=1
        return i-1