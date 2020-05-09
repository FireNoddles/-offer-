#给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针

#自己的思路不对 想的是递归 想复杂了
# 思路 如果这个节点有右孩子 直接找右孩子的最左节点
#如果 没有右孩子 往父节点找 1.父节点为空 说明是根节点 返空
# 2 必须找到左孩子的父节点 返回父节点 如果没有说明是树的节点最右边节点 返空
class Solution:
    def GetNext(self, pNode):
        if pNode.right != None:
            pNode = pNode.right
            while pNode.left != None:
                pNode = pNode.left
            return pNode
        else:
            if pNode.next != None:
                pNode_n = pNode.next
            else:
                return None
            while pNode_n.left != pNode:
                pNode = pNode_n
                if pNode_n.next != None:
                    pNode_n = pNode_n.next
                else:
                    return None

            return pNode_n