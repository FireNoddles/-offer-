# 数字在排序数组中出现的次数
# 计数排序 注意第一个条件不能交换次序 不行 还是On
class Solution:
    def GetNumberOfK(self, data, k):

        if len(data)==0 or k > data[len(data)-1]:
            return 0
        a = [0] * (data[len(data)-1]+1)
        for _ in data:
            a[_] += 1
        return a[k]


# 折半查找法 注意停止条件是<= Ologn
class Solution:
    def GetNumberOfK(self, data, k):
        if len(data)==0 or k > data[len(data)-1]:
            return 0
        return self.find(data,k+0.5)-self.find(data,k-0.5)
    def find(self,data, num):
        i = 0
        j = len(data)-1
        m = (i+j) // 2
        while i<=j:
            if data[m] < num:
                i = m+1
                m = (i+j) // 2
            else:
                j = m-1
                m = (i+j) // 2
        return i