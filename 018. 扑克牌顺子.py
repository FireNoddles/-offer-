# LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,
# 决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”
# (大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,
# 然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。


# 思路 排序， 统计0的个数 两个指针 相差1 当两个指针的数相差0或者超过当前0的个数 就返回失败
#当在0的个数以内时，0补足，两个指针加1
#当两个数差1 时  直接指针加1
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) == 0:
            return False
        num_of_goh = 0
        numbers = sorted(numbers)
        i = 0
        j = 1
        while(j<len(numbers)):
            if numbers[i] == 0:
                num_of_goh+=1
                i += 1
                j += 1
            else:
                if numbers[j]-numbers[i] - 1 > num_of_goh or numbers[j]-numbers[i]==0:
                    return False
                elif numbers[j]-numbers[i] == 1:
                    i += 1
                    j += 1
                else:
                    num_of_goh = num_of_goh - (numbers[j]-numbers[i]-1)
                    i += 1
                    j += 1
        return True


# 高级解法 可以看到 这组数在0-13 有范围的数 计数排序 如果一个数除0外的数出现两个 说明失败
# 这组数的最大值-最小值<5  成功
class Solution2:
    def IsContinuous(self, numbers):
        if len(numbers) == 0 or len(numbers)>5:
            return False
        d = [0] * 14
        min = 15
        max = -1
        for _ in numbers:
            if _ != 0:
                d[_] += 1
                if d[_] > 1:
                    return False
                if _ < min:
                    min = _
                if _ > max:
                    max = _
        if max - min < 5:
            return True
        else:
            return  False

a = Solution2()
print(a.IsContinuous([1,5,0,0,0]))