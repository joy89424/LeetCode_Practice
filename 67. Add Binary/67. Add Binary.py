class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        carry = 0 # 進位
        # 將前面填充0，使得長度一樣
        if len(a) < len(b):
            a = a.zfill(len(b))
        elif len(a) > len(b):
            b = b.zfill(len(a))
        
        # 從後面作加法
        for i in range(len(a)):
            # 加起來 = 0 -> 不需進位，且留下0
            if int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + carry == 0:
                sum = "0"+sum
                carry = 0
            # 加起來 = 1 -> 不需進位，且留下1
            elif int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + carry == 1:
                sum = "1"+sum
                carry = 0
            # 加起來 = 2 -> 需進1位，且留下1
            elif int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + carry == 2:
                sum = "0"+sum
                carry = 1
            # 加起來 = 3 -> 需進1位，且留下0
            else:
                sum = "1"+sum
                carry = 1
        if carry == 1:
            sum = "1"+sum
        return sum
