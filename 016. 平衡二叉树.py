# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
#
# 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树


# 求二叉树的深度 从上到下判断左右子树高度差
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        return (-2<self.deep(pRoot.left) - self.deep(pRoot.right) <2) & self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def deep(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        nLeft = self.deep(pRoot.left)
        nRight = self.deep(pRoot.right)
        return max(nLeft+1,nRight+1)
# 从底部向上扫 减少多次查找节点高度
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.balanceHeight(pRoot) >= 0

    def balanceHeight(self, root):
        if root is None:
            return 0
        left = self.balanceHeight(root.left)
        right = self.balanceHeight(root.right)

        if (left < 0 or right < 0 or abs(left - right) > 1):
            return -1
        return max(left, right) + 1