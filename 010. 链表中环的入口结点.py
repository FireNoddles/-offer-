#给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
#思路 遍历访问链表 记录地址 地址重复则为入口

class Solution:
    def EntryNodeOfLoop(self, pHead):
        li = []
        p = pHead
        while p!=None:
            if id(p) not in li:
                li.append(id(p))
                p = p.next
            else:
                return p