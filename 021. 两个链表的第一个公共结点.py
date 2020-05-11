# 输入两个链表，找出它们的第一个公共结点。（
# 注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
# 不理解什么是公共结点 --》就是Y字型链表 两个链表从某个节点开始为1个链表

#思路1 获取两个链表的长度 ，并求二者差a 让长的先走a步 剩下的长度二者一样 一起走 当两个指针相等时 就是公共节点
#
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        len1 = self.lenlist(pHead1)
        len2 = self.lenlist(pHead2)

        if len2 > len1:
            pHead1, pHead2 = pHead2, pHead1
        dis = abs(len1 - len2)
        p1 = pHead1
        while dis > 0:
            p1 = p1.next
            dis -= 1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def lenlist(self, p):
        len1 = 0
        while p.next != None:
            len1 += 1
            p = p.next
        return len1


# 思路2 和思路1一样 只不过不需要找长度 两个链表一起走 当短的链表指针a走完时，直接跳到长的链表的表头
#这时两个指针a,b都在长的链表上并且b-a的长度就是两个链表长度的差，
# 再当b走到结尾时，b指向短链表表头 两个一起走 当a，b节点相同时为公共节点

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        p1, p2 = pHead1, pHead2
        #while p1!=p2:
            # p1 = p1.next if p1!=None else pHead2
            # p2 = p2.next if p2!=None else pHead1
        while p1 != p2:
            if p1 != None:
                p1 = p1.next
            else:
                p1 = pHead2
            if p2 != None:
                p2 = p2.next
            else:
                p2 = pHead1

        return p1