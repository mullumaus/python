# 实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1/x * self.myPow(1/x, -n -1)
        if n % 2 == 0:
            return self.myPow(x * x,n/2)
        return x * self.myPow(x * x , n/2)
