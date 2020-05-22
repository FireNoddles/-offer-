#在一个字符串(0<=字符串长度<=10000，全部由字母组成)
# 中找到第一个只出现一次的字符,并返回它的位置,
# 如果没有则返回 -1（需要区分大小写）.（从0开始计数）

import collections
class Solution:
    def FirstNotRepeatingChar(self, s):
        dic = collections.OrderedDict()
        for _ in range(len(s)):
            if s[_] not in dic:
                dic[s[_]] = [1,_]
            else:
                dic[s[_]][0] += 1
        for _ in dic:
            if dic[_][0] == 1:
                return dic[_][1]
        return -1