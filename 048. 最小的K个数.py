# 输入n个整数，找出其中最小的K个数。
# 例如输入4,5,1,6,2,7,3,8这8个数字，
# 则最小的4个数字是1,2,3,4,。

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k>len(tinput) or k<=0:
            return []
        list1 = []
        #前k个数插入排序
        for _ in range(0,k):
            list1.append(tinput[_])
            for __ in range(_,0,-1):
                if list1[__] < list1[__-1]:
                    temp = list1[__-1]
                    list1[__-1] = list1[__]
                    list1[__] = temp
                else:
                    break
        # 后k个依次比较
        for ___ in range(k,len(tinput)):
            if tinput[___] < list1[-1]:
                list1[-1] = tinput[___]
                for t in range(k-1,0,-1):
                    if list1[t] < list1[t-1]:
                        temp = list1[t-1]
                        list1[t-1] = list1[t]
                        list1[t] = temp
                    else:
                        break
        return list1

#内置排序
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k>len(tinput) or k<=0:
            return []
        a = sorted(tinput)
        return a[:k]
