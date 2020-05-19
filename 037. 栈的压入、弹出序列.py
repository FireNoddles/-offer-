# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，
# 序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）

# 思路 新建一个栈 按照顺序入栈 如果等于弹出序列就出栈

class Solution:
    def IsPopOrder(self, pushV, popV):
        list_1 = []
        for _ in pushV:
            list_1.append(_)
            while list_1[-1] == popV[0]:
                list_1.pop()
                del popV[0]
                if len(popV) == 0:
                    break
        if len(list_1)==0:
            return True
        else:
            return False
a = Solution()
print(a.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))