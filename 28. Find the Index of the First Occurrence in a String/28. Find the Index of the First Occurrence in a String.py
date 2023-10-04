class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        current = 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[:len(needle)] == needle:
                return current
            else:
                current+=1
                haystack = haystack[1:]
        return -1