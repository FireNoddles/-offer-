# https://www.nowcoder.com/questionTerminal/57d85990ba5b440ab888fc72b0751bf8?f=discussion
#根据公式 计算 当每段的取值在e时 乘积最大 而当等于2时的值小于等于3 所以分成当
# n≤3时，只有
# 当n==2时f(x)=1；
# 当n==3时f(x)=2;
# n≥3时，有
# 即n%3==0, n%3==1, n%3==2
# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        if number == 2:
            return 1
        elif number ==3:
            return 2
        elif number % 3 == 0:
            return 3 ** (number / 3)
        elif number %3 == 1:
            return 4 * (3 ** ((number // 3)-1))
        elif number %3 == 2:
            return 2* (3 ** (number // 3))
        # write code here