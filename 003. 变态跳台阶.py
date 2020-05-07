#一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
            return 1 << (number - 1)


#思路 假设链接：https://www.nowcoder.com/questionTerminal/22243d016f6b47f2a6928b4313c85387?f=discussion
# 因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
# 跳1级，剩下n-1级，则剩下跳法是f(n-1)
# 跳2级，剩下n-2级，则剩下跳法是f(n-2)
# 所以f(n)=f(n-1)+f(n-2)+...+f(1) + 1 # 加1为直接跳上去
# 因为f(n-1)=f(n-2)+f(n-3)+...+f(1)+1
# 所以f(n)=2*f(n-1) = 2^(n-1) * f(1) =2^(n-1) * 1
# f(1) =1
# 左移一位相当于* 2 因此用了 1 << (number - 1)