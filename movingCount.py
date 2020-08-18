# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def getNumberSum(self, row,col):
        res = 0
        while row>0:
            res += row % 10
            row //= 10
        while col>0:
            res += col % 10
            col //= 10
        return res

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if(k==0):
            return 1
        passed = set()
        q = []
        q.append((0,0))
        while q:
            x,y = q.pop(0)
            if (x,y) not in passed and self.getNumberSum(x,y) <=k:
                passed.add((x,y))
                for dx,dy in [(1,0),(0,1)]:
                    if 0 <= x + dx < m and 0<= y + dy < n:
                        q.append((x+dx,y+dy))
        return len(passed)

