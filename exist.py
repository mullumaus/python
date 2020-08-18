# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
#
# [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
#
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
#
#  
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def deepthFirstSearh(i,j,k):
            if not 0<=i<len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) -1 :
                return True
            tmp, board[i][j] = board[i][j],'/'
            res = deepthFirstSearh(i+1,j,k+1) or deepthFirstSearh(i-1,j,k+1) or deepthFirstSearh(i,j+1,k) or deepthFirstSearh(i,j-1,k)
            board[i][j]=tmp
            return res

        for i in range(len(board)):
            for j in range(len(board(0))):
                if deepthFirstSearh(i,j,0):
                    return True
        return False
