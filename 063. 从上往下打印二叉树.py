# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
# 层次遍历
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def __init__(self):
        self.result = []
        self.queue = []
    def PrintFromTopToBottom(self, root):
        if root == None:
            return []
        self.queue.append(root)
        while self.queue:
            a = self.queue[0]
            self.result.append(a.val)
            if a.left:
                self.queue.append(a.left)
            if a.right:
                self.queue.append(a.right)
            del self.queue[0]
        return self.result