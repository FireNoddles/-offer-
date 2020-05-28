# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 输入描述:
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

class Solution:
    def __init__(self):
        self.result = []
    def Permutation(self, ss):
        new_ss = [i for i in ss]
        self.Per(new_ss,0)
        #处理返回顺序
        return sorted(self.result)
    def reverse(self,newss):
        temp = ''
        for _ in newss:
            temp += _
        return temp
    def Per(self, new_ss, i):
        if i==(len(new_ss)-1):
            temp = self.reverse(new_ss)
            # 处理重复
            if temp not in self.result:
                self.result.append(temp)
            print(self.result)
        else:
            for _ in range(i,len(new_ss)):
                new_ss[_],new_ss[i] = new_ss[i],new_ss[_]
                self.Per(new_ss, i+1)
                #还原位置
                new_ss[_],new_ss[i] = new_ss[i],new_ss[_]

a = Solution()
print(a.Permutation('abc'))