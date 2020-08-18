# 请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，
# 有 2 位是 1。因此，如果输入 9，则该函数输出 2。


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight2(self,n):
        res = 0
        while n > 0:
            res += 1
            n &= n -1
        return res
