#输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。

#链接：https://www.nowcoder.com/questionTerminal/8fecd3f8ba334add803bf2a06af1b993?answerType=1&f=discussion
# 来源：牛客网
#
# http://blog.csdn.net/fanzitao/article/details/7895344
# 只是看一下解析，比较关键的一句话 所以在这里自定义一个比较大小的函数，
# 比较两个字符串s1, s2大小的时候，先将它们拼接起来，比较s1+s2,和s2+s1那个大，
# 如果s1+s2大，那说明s2应该放前面，所以按这个规则，s2就应该排在s1前面。 ，
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == []:
            return ""
        #冒泡思想
        for _ in range(0,len(numbers)):
            for __ in range(_+1,len(numbers)):
                a1 = int(str(numbers[_])+str(numbers[__]))
                a2 = int(str(numbers[__])+str(numbers[_]))
                if a1>a2:
                    numbers[_],numbers[__] = numbers[__],numbers[_]
        c=''
        for _ in numbers:
            c += str(_)
        return int(c)

a = Solution()
print(a.PrintMinNumber([3,5,1,4,2]))