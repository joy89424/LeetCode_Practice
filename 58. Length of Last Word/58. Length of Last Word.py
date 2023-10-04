class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 清除尾端空格
        while 1:
            if s[-1] != " ":
                break
            elif s[-1] == " ":
                s = s[:-1]
        # 從尾端讀到空格，就將s=空格到最後
        for i in range(len(s)):
            if s[len(s)-1-i] == " ":
                s = s[len(s)-i:]
                break
        return(len(s))
