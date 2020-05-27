# #将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
# 数值为0或者字符串不是一个合法的数值则返回0
# 输入描述:
# 输入一个字符串,包括数字字母符号,可以为空
# 输出描述:
# 如果是合法的数值表达则返回该数字，否则返回0
# 示例1
# 输入
# +2147483647
# 1a33
# 输出
# 2147483647
# 0

class Solution:
    def StrToInt(self, s):
        if s == '':
            return 0
        if s[0] == '+':
            s = s[1:]
        neg = 0
        if s[0] == '-':
            neg = 1
            s = s[1:]
        result = 0
        for _ in range(len(s)):
            if s[_] not in '0123456789':
                return 0
            else:  # if s[i]>='0' and s[i]<='9': 单个数字字符串可以这么比较
                c = 10**(len(s)-1-_)
                result += int(s[_])*c
        if neg==1:
            return -result
        else:
            return result

