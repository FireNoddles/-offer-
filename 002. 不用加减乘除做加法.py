#写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215?tpId=13&tqId=11201&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
#自己的想法 把两个数放到列表里 求和 投机取巧了
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        A = []
        A.append(num1)
        A.append(num2)
        return sum(A) #直接sum([num1,num2])

# 别人的想法 用位运算
#两个数的二进制相异或 相当于没有进位的加法 两个数的二进制相与并左移一位：相当于求得进位
#将上面两个过程相加 求得结果
#过程 先异或 得到没有进位的值 在与 得到进位 这里要左移一位<<1 因为是要给前一个数加1
# 再将两个值相加 因为可能进位加之后 还需要进位 因此一直异或和与 直到进位全为0
class Solution:
    def Add(self, a, b):
        while(b):
            # 0xFFFFFFFF 对负数的处理 使其不越界
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)

#补充 异或的另一个用法 两个数交换 不用temp
# a=a^b; 使用a本身作为一个temp 其为二者的异或值
# b=b^a; 将a赋给b
# a=b^a; b赋给a

#原因 异或时两个不同的值为1 而任何值与1异或为其相反的值 0^1 = 1 （相当于取反再取反 就是其本身）
# 异或时两个相同的值为0 而任何值与0异或为其本身值 0^1 = 1 （相当于相同再相同 就是其本身）