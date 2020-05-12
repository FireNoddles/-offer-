# 一只青蛙一次可以跳上1级台阶，
# 也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法
# （先后次序不同算不同的结果）。

# 斐波那契数列

class Solution:
    def jumpFloor(self, number):
        if number < 4:
            return number
        pre = 2
        las = 3
        for i in range(4, number + 1):
            las = pre + las
            pre = las - pre
        return las