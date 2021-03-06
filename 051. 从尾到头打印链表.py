# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。


#1. 利用插入指定位置
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result = []
        while listNode!=None:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result


# 2. 递归到最后一个再逐层添加值
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.result = []
    def printListFromTailToHead(self, listNode):
        if listNode==None:
            return []
        self.deep(listNode)
        return self.result
    def deep(self, listNode):
        if listNode.next!=None:
            self.deep(listNode.next)
        self.result.append(listNode.val)