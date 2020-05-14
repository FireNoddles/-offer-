# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# 二进制中 1和另一个数相与都为其它数 0和其它数相与都是0
# 在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
class Solution:
    def NumberOf1(self, n):
        return sum([n >> i & 1 for i in range(32)])


n = -1
print(bin(n))
print( bin(n& 0xffffffff))