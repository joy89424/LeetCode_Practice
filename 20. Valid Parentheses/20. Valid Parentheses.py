class Solution:
    def isValid(self, s: str) -> bool:
        key_dict = {
            "(" : ")"
            ,"{" : "}"
            ,"[" : "]"
            ,")" : ""  #避免傳入未知參數報錯
            ,"}" : ""
            ,"]" : ""}
        stack = []
        i = 0
        print("len = ", len(s))
        while i < len(s):
            if stack == []: # 如果stack為空，就必加入stack()
                stack.append(s[i])
            elif key_dict[stack[-1]] != s[i]: # 如果stack最後一項跟現在這項是一組，stack()就不加入
                stack.append(s[i])            # 換句話說就是stack最後一項跟現在這項不是一組，stack()就加入
            
            if key_dict[stack[-1]] == s[i]: # 如果stack最後一項跟現在這項是一組，就pop()
                stack.pop()
                i+=1
            elif i != len(s)-1: 
                if key_dict[s[i]] == s[i+1]: # 如果s這項跟s下一項是一組，就pop()
                    stack.pop()
                    i+=2 
                else:
                    i+=1
            else:
                i+=1
        #print("stack = ", stack)
        if stack == []:
            return True
        else:
            return False
