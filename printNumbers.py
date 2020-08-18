# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        max = 10 ** n
        res = []
        i = 1
        while i < max:
            res.append(i)
            i += 1
        return res
