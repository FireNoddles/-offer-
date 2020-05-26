# python 2.7不可用
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