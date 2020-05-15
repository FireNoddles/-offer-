# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#
# 保证base和exponent不同时为0


# 快速幂
class Solution:
    def Power(self, base, exponent):
        if exponent<0:
            e = -exponent
        elif exponent==0:
            if base == 0:
                return False
            else:
                return 1
        else:
            e = exponent
        re = 1
        t = base
        while e>0:
            if e & 1 == 1:
                re = re * t
                print(re)
            t = t * t
            e = e >> 1
        if exponent<0:
            return 1/re
        else:
            return re

a = Solution()
print(a.Power(2,4))


# 递归
# 链接：https://www.nowcoder.com/questionTerminal/1a834e5e3e1a4b7ba251417554e07c00?answerType=1&f=discussion
# 来源：牛客网
#
# 解法 3: 二分法
# 为了方便讨论，假设指数exponent是正数。那么递归式如下：
#
# 如果exponent是偶数，Power(base, exponent) = Power(base, exponent / 2) * Power(base, exponent / 2)
# 如果exponent是奇数，Power(base, exponent) = base * Power(base, exponent / 2) * Power(base, exponent / 2)
# 对于负指数exponent的情况，取其绝对值先计算。将最后结果取倒数即可。
#
# 时间复杂度是 O(logN)；由于采用递归结构，空间复杂度是 O(logN)。
#
# // 原文地址：https://xxoo521.com/2019-12-31-pow/
# // ac地址：https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00
#
# function Power(base, exponent) {
#     const isNegative = exponent < 0; // 是否是负指数
#     const result = absPower(base, Math.abs(exponent));
#     return isNegative ? 1 / result : result;
# }
#
# function absPower(base, exponent) {
#     if (exponent === 0) {
#         return 1;
#     }
#
#     if (exponent === 1) {
#         return base;
#     }
#
#     const subResult = absPower(base, Math.floor(exponent / 2));
#     return exponent % 2 ? subResult * subResult * base : subResult * subResult;
# }