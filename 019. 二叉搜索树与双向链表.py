#输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

#我的思想：中序遍历 得到结果 再链接
class Solution:
    def __init__(self):
        self.mid = []
    def deep(self,pRootOfTree):
        if pRootOfTree==None:
            return
        self.deep(pRootOfTree.left)
        self.mid.append(pRootOfTree)
        self.deep(pRootOfTree.right)
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return pRootOfTree
        self.deep(pRootOfTree)
        for _ in range(len(self.mid) -1 ):
            self.mid[_].right = self.mid[_+1]
            self.mid[_+1].left = self.mid[_]
        return self.mid[0]