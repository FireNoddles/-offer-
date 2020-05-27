# 请实现一个函数，用来判断一颗二叉树是不是对称的。
# 注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


#比较的是一个结点的左孩子和一个结点的右孩子  以及 一个结点的右孩子和一个结点的左孩子
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot == None:
            return True
        else:
            return self.deep(pRoot.left, pRoot.right)
    def deep(self, l, r):
        if l == None and r == None:
            return True
        if (l and r == None) or (r and l == None) or l.val != r.val:
            return False
        else:
            if self.deep(l.left,r.right) and self.deep(l.right,r.left):##比较的是一个结点的左孩子和一个结点的右孩子  以及 一个结点的右孩子和一个结点的左孩子
                return True
            else:
                return False