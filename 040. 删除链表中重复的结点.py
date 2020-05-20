# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
# 重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


# 新增一个结点在数的前面
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        new = ListNode(None)
        pre = new
        pre.next = pHead
        mi = pHead
        while mi:
            if mi.next and mi.next.val == mi.val:
                while mi.next and mi.next.val == mi.val:
                    mi = mi.next
                pre.next = mi.next
                mi = mi.next
            else:
                pre.next = mi
                pre = mi
                mi = mi.next
        return new.next