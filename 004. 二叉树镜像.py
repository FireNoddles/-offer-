#题目描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 输入描述:
# 二叉树的镜像定义：源二叉树
#     	    8
#     	   /  \
#     	  6   10
#     	 / \  / \
#     	5  7 9 11
#     	镜像二叉树
#     	    8
#     	   /  \
#     	  10   6
#     	 / \  / \
#     	11 9 7  5

#自己思路 递归 和别人解法类似 如果存在左子树或右子树就交换
# 注意类里面递归的格式 self.function 传递参数不用再加self
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None: return root
        if root.left != None or root.right != None:
            temp = root.left
            root.left = root.right
            root.right =temp
            if root.left != None:
                self.Mirror(root.left)# 注意类里面递归的格式 self.function 传递参数不用再加self
            if root.right != None:
                self.Mirror(root.right)
        else:
            return root
        # write code here
