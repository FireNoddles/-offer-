# 输入一个链表，输出该链表中倒数第k个结点。

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return head
        if k<=0:
            return None
        #两个指针 第一个先走k步
        pre = head
        m = head
        #先走k步
        while k > 0:
            pre = pre.next
            k -= 1
            #超过链表长
            if not pre:
                if k!=0:
                    return None
        #一起走
        while pre:
            pre = pre.next
            m = m.next
        return m