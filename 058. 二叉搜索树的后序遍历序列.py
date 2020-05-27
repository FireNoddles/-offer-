# python 2.7不可用
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

#链接：https://www.nowcoder.com/questionTerminal/a861533d45854474ac791d90e447bafd?f=discussion

# BST的后序序列的合法序列是，对于一个序列S，
# 最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，
# 那么T满足：T可以分成两段，前一段（左子树）小于x，
# 后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if self.deep(sequence):
            return 1
        else:
            return 0
    def deep(self, sequence):
        if not sequence:
            return False
        if len(sequence)<=1:
            return True
        mid = sequence[-1]
        a1 = []
        a2 = []
        j = -1
        for _ in range(len(sequence)):
            if sequence[_] > mid:
                j = _ - 1
                break
        if j!=-1:
            a1.extend(sequence[0:j+1])
        a2.extend(sequence[j+1:-1])
        for _ in a2:
            if _ < mid:
                return False
        if self.VerifySquenceOfBST(a1) and self.VerifySquenceOfBST(a2):
            return True
        else:
            return False



class Solution:
    def VerifySquenceOfBST(self, sequence):
        if self.deep(sequence):
            return 1
        else:
            return 0
    def deep(self, sequence):
        if not sequence:
            return False
        if len(sequence)<=1:
            return True
        mid = sequence[-1]
        j = 0
        while  sequence[j]<mid:
            j+=1
        a1=sequence[0:j]
        a2=sequence[j:-1]
        for _ in a2:
            if _ < mid:
                return False
        t = True
        t2 = True
        if len(a1)>0:
            t = self.VerifySquenceOfBST(a1)
        if len(a2)>0:
            t2 = self.VerifySquenceOfBST(a2)
        return t and t2
a = Solution()
print(a.VerifySquenceOfBST([4,6,7,5]))