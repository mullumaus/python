#输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.dict, self.po = {}, preorder
        for i in range (len(inorder)):
            self.dict[inorder[i]] = i
        return self.recur(0,0,len(inorder)-1)


    def recur(self,pre_root,in_left, in_right):
        if in_left > in_right: # 终止条件：中序遍历为空
            return
        root = TreeNode(self.po[pre_root]) # 建立当前子树的根节点
        i = self.dict[self.po[pre_root]]  # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root+1,in_left,i)
        root.right = self.recur(i-in_left+pre_root+1,i+1,in_right)
        return  root
