#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# -*- coding:utf-8 -*-
#有思路 不会写
# 思路 入对直接放到栈1里 出队时如果栈2里有数就弹出
# 没数就把栈1的数挨个弹出放到栈2 再弹出
class Solution:
    #首先要定义两个栈 初始化形式
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)
        return self.stack1

    def pop(self):
        #如果栈2不为空 弹出
        if self.stack2 != []:
            # list_numa.pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
            return self.stack2.pop()
        # 如果为空 栈1放入栈2
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            out = self.stack2.pop()
            return out