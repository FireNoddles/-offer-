# 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。



#使用一个列表保存当前的路径 最后的叶子节点等于目标值就加到最终结果里

# 注意： 每一个新节点要new一个新列表并保存之前的结果 否则都是加到同一个列表里
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.road = []

    def FindPath(self, root, expectNumber):
        if not root or expectNumber <= 0:
            return []
        path = []
        self.deep(root, expectNumber, path)
        return self.road

    def deep(self, root, expectNumber, path):
        if root.val > expectNumber:
            return
        # 注意： 每一个新节点要new一个新列表并保存之前的结果 否则都是加到同一个列表里
        new_path = path[:]
        new_path.append(root.val)
        if root.val == expectNumber and root.left == None and root.right == None:
            self.road.append(new_path)
        if root.left:
            self.deep(root.left, expectNumber - root.val, new_path)
        if root.right:
            self.deep(root.right, expectNumber - root.val, new_path)