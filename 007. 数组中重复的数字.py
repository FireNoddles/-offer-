#在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，
# 但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
# 那么对应的输出是第一个重复的数字2。


# 思路先排序 找重复（自己编译器可以 nowcode过不去 不知道为什么）
class Solution:
# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
# 函数返回True/False
    def duplicate(self, numbers, duplication):
        if numbers<=1: return False
        dump = sorted(duplication)
        i = 0
        j = 1
        flag = 1
        while flag == 1:
            if dump[i] == dump[j]:
                break
            elif j>numbers:
                return False
            else:
                i+=1
                j+=1
        duplication[0] = dump[j]
        return True

# 高级思路 哈希 题目没有看清 几个数字都在n以内 可以建立一个新表
# 对应访问过的数字在表的下标置访问过的标记，再次访问就会被发现。
class Solution2:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if len(numbers)<=1: return False
        flag = [0] * len(numbers)
        print(flag)
        i = 0
        while i<len(numbers):
            print(numbers[i])
            if flag[numbers[i]] == 0:
                flag[numbers[i]] = 1
                i+=1
            elif flag[numbers[i]] == 1:
                duplication[0] = numbers[i]
                return True
            print(flag)
        return False