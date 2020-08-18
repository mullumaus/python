# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return False
        transTable = [
            [1, 2, 7, -1, -1, 0],
            [-1, 2, 7, -1, -1, -1],
            [-1, 2, 3, 4, -1, 9],
            [-1, 3, -1, 4, -1, 9],
            [6, 5, -1, -1, -1, -1],
            [-1, 5, -1, -1, -1, 9],
            [-1, 5, -1, -1, -1, -1],
            [-1, 8, -1, -1, -1, -1],
            [-1, 8, -1, 4, -1, 9],
            [-1, -1, -1, -1, -1, 9]
        ]



        def get_col(c):
            dict = {
                "sign": 0,
                "number": 1,
                ".": 2,
                "exp": 3,
                "other": 4,
                "blank": 5
            }
            if c.isdigit(): key = 'number'
            elif c in {'+','-'}: key = 'sign'
            elif c =='.': key = '.'
            elif c in {'e','E'}: key = 'exp'
            elif c == ' ': key = 'blank'
            else: key = 'other'
            return dict[key]

        legal_state = {2,3,5,8,9}
        state = 0
        for c in s:
            col = get_col(c)
            state = transTable[state][col]
            if state == -1:
                return False
        if state in legal_state:
            return True
        return False
