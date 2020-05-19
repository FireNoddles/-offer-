# 输入一个链表，反转链表后，输出新链表的表头。

#栈
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None:
            return pHead
        temp = []
        p = pHead
        while p:
            temp.append(p)
            p = p.next
        re = temp[len(temp)-1]
        while len(temp)!=0:
            temp2 = temp.pop()
            if len(temp)-1 >= 0:
                temp2.next = temp[len(temp)-1]
            else:
                temp2.next= None
        return re

# 三指针
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre = None
        while pHead:
            rear = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = rear

        return pre