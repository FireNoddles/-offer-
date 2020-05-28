# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
class Solution:
    # s字符串
    def isNumeric(self, s):
        flag_poit = 0
        flag_e = 0
        for _ in range(len(s)):
            # 判断首位
            if _ == 0:
                if s[_] not in '+-0123456789':
                    return False
            else:
                # 如果不是数字
                if s[_] not in '0123456789':
                    #如果是. 计数器加1
                    if s[_] == '.':
                        flag_poit+=1
                        #如果是末尾· 或者出现2次点或者在e后面出现. 失败
                        if _ == (len(s) - 1) or flag_poit>1 or flag_e==1:
                            return False
                        # 如果·后或前没有数字 失败
                        if s[_ + 1] not in '0123456789' and s[_ - 1] not in '0123456789':
                            return False
                    # 如果是e 计数器加1
                    elif s[_] == 'E' or s[_] == 'e':
                        flag_e+=1
                        #如果是末尾e 或者出现2个e 失败
                        if _ == (len(s)-1) or flag_e>1:
                            return False
                        # 如果E后或前没有数字 失败
                        if s[_ + 1] not in '-0123456789' and s[_-1] not in '0123456789':
                            return False
                    # 如果是+-号 由于不是首位 则前面必须要有E
                    elif s[_] == '-' or s[_] == '+':
                        if s[_-1] != 'E' and s[_-1] !='e':
                            return False
                    # 是其它字符 失败
                    else:
                        return False
        return True

a = Solution()
print(a.isNumeric("1a3.14"))