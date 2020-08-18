# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        row = len(matrix)
        column = len(matrix[0])
        x = 0
        y = column - 1
        while ( x < row and y >= 0):
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y = y -1
            if matrix[x][y] < target:
                x = x + 1
        return False


