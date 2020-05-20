# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
# {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
# {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

# O n*size
class Solution:
    def maxInWindows(self, num, size):
        i = 0
        j = size
        re = []
        while j <= len(num):
            temp = [num[i] for i in range(i,j)]
            print(temp)
            re.append(max(temp))
            i+=1
            j+=1
        return re

#链接：https://www.nowcoder.com/questionTerminal/1624bc35a45c42c0bc17d17fa0cba788?answerType=1&f=discussion
# 来源：牛客网
#
# 思路：建立一个两端开口的队列，放置所有可能是最大值的数字（存放的其实是最大值的下标），队首记录的是最大值的下标。从头开始扫描数组：
#
# 1.如果遇到的数字比队列中所有的数字都大，那么它就是最大值，其它数字不可能是最大值了，将队列中的所有数字清空，放入该数字。（在尾部添加的）
# 2.如果遇到的数字比队列中的所有数字都小，那么它还有可能成为之后滑动窗口的最大值，放入队列的末尾
# 3.如果遇到的数字比队列中最大值小，最小值大，那么将比它小数字不可能成为最大值了，删除较小的数字，放入该数字。
# 由于滑动窗口有大小，因此，队列头部的数字如果其下标离滑动窗口末尾的距离大于窗口大小，那么也删除队列头部的数字。
# On
class Solution:
    def maxInWindows(self, num, size):
        if size <=0 or size > len(num):
            return []
        list1 = []
        result = []
        i = 0
        while i < len(num):
            if len(list1)>0 and i-size+1 > list1[0]:
                del list1[0]
            while len(list1)>0 and num[list1[-1]]< num[i]:
                list1.pop()
            list1.append(i)
            i+=1
            if i > size - 1:
                result.append(num[list1[0]])
        return result
