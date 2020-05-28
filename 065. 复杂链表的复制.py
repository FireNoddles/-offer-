# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
# 另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，
# 并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，
# 否则判题程序会直接返回空）



# 1、复制每个节点，如：复制节点A得到A1，将A1插入节点A后面
#         2、遍历链表，A1->random = A->random->next; 注意判断有没有random
#         3、将链表拆分成原链表和复制后的链表 # 注意保持原链
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        init = pHead
        while(pHead):
            node = RandomListNode(pHead.label)
            node.next = pHead.next
            pHead.next = node
            pHead = node.next
        pHead = init
        while(pHead):
            p = pHead.next
            if pHead.random:
                p.random = pHead.random.next
            pHead = p.next
        pHead = init
        pNode=pHead
        pClonedHead=None
        pCloned=None
        if pHead:
            pClonedHead=pCloned=pNode.next
            pNode.next=pCloned.next
            pNode=pCloned.next
        # 原链也需要保持
        while pNode:
            pCloned.next = pNode.next
            pCloned=pCloned.next
            pNode.next=pCloned.next
            pNode=pCloned.next
        return pClonedHead