#实现一个函数，把字符串 s 中的每个空格替换成"%20"。
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        rstr = ""
        for i in s:
            if i == ' ':
                rstr = rstr + "%20"
            else:
                rstr = rstr + i
        return rstr
