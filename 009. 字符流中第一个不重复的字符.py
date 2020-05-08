#请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
# -*- coding:utf-8 -*-
# 插入时使用计数器进行计数 注意 由于字典的读取并不是按插入的顺序 因此在检查计数时要按字符串的顺序
class Solution:
    # 返回对应char
    def __init__(self):
        self.s =''
        self.dic = {}
    def FirstAppearingOnce(self):
        for _ in self.s:
            if self.dic[_] == 1:
                return _
        return '#'
        # write code here
    def Insert(self, char):
        self.s = self.s + char
        if char in self.dic:
            self.dic[char] = self.dic[char]+ 1
        else:
            self.dic[char]=1
        # write code here
