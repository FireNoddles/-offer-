# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

#1, 调用函数
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = s.replace(' ', '%20')
        return s

# 开辟新内存
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        re = ''
        for _ in s:
            if _ != ' ':
                re += _
            else:
                re += '%20'

        return re

# 生成器
def st(s):
    result =''
    for _ in s:
        if _ == ' ':
            result+='%20'
        else:
            result+=_
        yield result

def replaceSpace(s):
    s1 = st(s)
    for _ in s:
        s = next(s1)

    print(s)

replaceSpace('h3ll llo llu ')