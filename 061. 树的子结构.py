
# 两次递归 第一次递归找到相同的初始点开始第二次递归
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        a = False
        if pRoot1.val == pRoot2.val:
            a = self.deep(pRoot1, pRoot2)
        if a == False:
            a = self.HasSubtree(pRoot1.left, pRoot2)
        if a == False:
            a = self.HasSubtree(pRoot1.right, pRoot2)
        return a
    def deep(self, pRoot1, pRoot2):
        if not pRoot2: # 如果子树空了 说明全部找完了
            return True
        if not pRoot1:# 如果被匹配的树空了 说明匹配不完
            return False
        if pRoot1.val != pRoot2.val:# 不等 失败
            return False
        return self.deep(pRoot1.left,pRoot2.left) and self.deep(pRoot1.right,pRoot2.right)