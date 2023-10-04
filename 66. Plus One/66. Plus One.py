class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 轉為 sting 方便做處理
        str_digits = str(digits)
        str_digits = str_digits.replace(",","") # 去除 ,
        str_digits = str_digits.replace(" ","") # 去除 空格
        str_digits = str_digits[1:-1]           # 去除 [ ]

        # 轉為 int 方便做計算
        int_digits = int(str_digits)+1

        # 轉為 sting 方便做處理
        str_digits = str(int_digits)
        output_list = []
        for i in range(len(str_digits)):
            output_list.append(int(str_digits[i]))
        return output_list
