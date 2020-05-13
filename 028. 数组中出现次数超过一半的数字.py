#数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

#自己的思路 暴力法 统计个数 输出 略去

# 可以先排一次序 排序完的数组中间的数一定满足要求（比如：1，2，2，2，3；或2，2，2，3，4；或2，3，4，4，4等等）复杂度nlogn
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        numbers = sorted(numbers)
        i = 0
        for _ in numbers:
            if _ == numbers[len(numbers)//2]:
                i+=1
        if i>(len(numbers)//2):
            return numbers[len(numbers)//2]
        else:
            return 0


# On复杂度 链接：https://www.nowcoder.com/questionTerminal/e8a1b01a2df14cb2b228b30ee6a92163?answerType=1&f=discussion
# 来源：牛客网
#
# 用preValue记录上一次访问的值，
# count表明当前值出现的次数，如果下一个值和当前值相同那么count++；如果不同count--，
# 减到0的时候就要更换新的preValue值了，因为如果存在超过数组长度一半的值，那么最后preValue一定会是该值。
#注意的是 需要判断是否真的是大于1半数，这一步骤是非常有必要的，
# 因为我们的上一次遍历只是保证如果存在超过一半的数就是preValue，但不代表preValue一定会超过一半

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        val = numbers[0]
        times = 1
        i = 0
        for _ in numbers:
            if times == 0:
                val = _
                times = 1
            elif val == _:
                times +=1
            elif val!=_:
                times-=1
        for _ in numbers:
            if _ == val:
                i+=1
        if i>(len(numbers)//2):
            return numbers[len(numbers)//2]
        else:
            return 0