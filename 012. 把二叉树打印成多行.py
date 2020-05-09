# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
#思路 用队列 先把根放进队列 开始遍历 每次从队列里挨个取 有孩子就放进temp暂时保存 最后队列 = temp
#直到队列为空结束
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot == None:
            return []
        result = []
        arr = []
        arr.append(pRoot)
        while len(arr)!=0:
            result.append([i.val for i in arr])
            temp = []
            for _ in arr:
                if _.left!=None:
                    temp.append(_.left)
                if _.right!=None:
                    temp.append(_.right)
            arr = temp
        return result