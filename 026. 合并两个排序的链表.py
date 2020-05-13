# 输入两个单调递增的链表，
# 输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。
# -*- coding:utf-8 -*-

#注意新建一个结点的语句 非递归版本
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def Merge(self, pHead1, pHead2):
    p = ListNode(None)
    head = p
    while pHead1 and pHead2:
        if pHead1.val < pHead2.val:
            p.next = pHead1
            pHead1 = pHead1.next

        else:
            p.next = pHead2
            pHead2 = pHead2.next
        p = p.next

    if pHead1 != None:
        p.next = pHead1
    if pHead2 != None:
        p.next = pHead2
    return head.next