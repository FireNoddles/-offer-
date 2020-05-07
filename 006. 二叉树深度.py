#输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
#递归
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None : return 0
        if pRoot.left!=None:
            left = self.TreeDepth(pRoot.left)+1
        else:
            left = 1
        if pRoot.right!=None:
            right = self.TreeDepth(pRoot.right)+1
        else:
            right = 1
        return max([left,right])