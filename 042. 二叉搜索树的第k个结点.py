#给定一棵二叉搜索树，
# 请找出其中的第k小的结点。
# 例如， （5，3，7，2，4，6，8）
# 中，按结点数值大小顺序第三小结点的值为4。

#注意 二叉搜索树就是二叉排序树
#中序遍历 直接返回第k个

class Solution:
    def __init__(self):
        self.list1 = []

    # 返回对应节点TreeNode
    def mid(self, pRoot):
        if pRoot == None:
            return
        self.mid(pRoot.left)
        self.list1.append(pRoot)
        self.mid(pRoot.right)

    def KthNode(self, pRoot, k):
        self.mid(pRoot)
        if len(self.list1) < k or k <= 0:
            return None
        return self.list1[k - 1]