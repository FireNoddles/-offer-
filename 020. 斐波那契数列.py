#大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
# 使用递归 不合格 超时
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = self.Fibonacci(n-1) + self.Fibonacci(n-2)
            return result

a = Solution()
print(a.Fibonacci(36))


#非递归 存储On
class Solution:
    def Fibonacci(self, n):
        if n < 2: return n
        list1 = [0] * (n+1)
        for _ in range(n+1):
            if _ <2:
                list1[_] = _
            else:
                list1[_] = list1[_-1] + list1[_-2]
        return list1[n]

#非递归 存储最近的两个数
class Solution:
    def Fibonacci(self, n):
        if n < 2: return n
        list1 = [0] * 2
        for _ in range(n+1):
            if _ <2:
                list1[_] = _
            else:
                sum = list1[0] + list1[1]
                list1[0] = list1[1]
                list1[1] = sum
        return sum

#非递归 存储最近的1个数
class Solution:
    def Fibonacci(self, n):
        if n < 2: return n
        list1 = [0,1]
        for _ in range(2,n+1):
            list1[1] = list1[1] + list1[0]
            list1[0] = list1[1] - list1[0]
        return list1[1]