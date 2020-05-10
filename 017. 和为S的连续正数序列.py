#题目描述
# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
# 输出描述:
# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
# 思路 假设初始为x 则有x+x+1+x+2+....+x+n-1 = nx+n(n-1)/2 = s ==> x = s/n - (n-1)/2 根据这个关系求解
# 以下代码在编译器中可以通过 思路应该没问题 但是太复杂
class Solution:
    def FindContinuousSequence(self, tsum):
        result = []
        for n in range(2,tsum):
            x = tsum/n - (n-1)/2
            print(x)
            if int(x) == x and  x>0:
                temp = []
                for _ in range(n):
                    temp.append(x+(_*1))
                result.append(temp)
        result = sorted(result,key = lambda x: x[0])
        return result

# 新思路 双指针技术，就是相当于有一个窗口，
# 窗口的左右两边就是两个指针，我们根据窗口内值之和来确定窗口的位置和宽度。

class Solution:
    def FindContinuousSequence(self, tsum):
        result = []
        left= 1
        right= 2
        while(left < right):
            if (left + right)* (right- left +1)/2 == tsum:
                temp = []
                for _ in range(left, right+1):
                    temp.append(_)
                result.append(temp)
                right+=1
            elif (left + right)* (right- left +1)/2 < tsum:
                right+=1
            elif (left + right)* (right- left +1)/2 > tsum:
                left+=1
        return result