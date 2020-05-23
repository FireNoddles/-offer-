#定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
#注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

#需要注意的是要保存每轮入栈之后的最小值 以防出栈之后找不到当前栈的最小值

class Solution:
    def __init__(self):
        self.list1 = []
        self.min1 = []
    def push(self, node):
        self.list1.append(node)
        if len(self.min1) == 0 or node < self.min1[-1]:
            self.min1.append(node)
        # write code here
    def pop(self):
        a = self.list1[-1]
        if a == self.min1[-1]:
            self.min1.pop()
        self.list1.pop()
        # write code here
    def top(self):
        return self.list1[-1]
        # write code here
    def min(self):
        return self.min1[-1]