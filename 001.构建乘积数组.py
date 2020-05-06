#链接：https://www.nowcoder.com/questionTerminal/94a4d381a68b47b7a8bed86f2975db46?f=discussion
#给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
# （注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）

# 自己的想法 暴力破解 即把每一行的数乘起来（对于B[i],A[i]不乘)
class Solution:
    def multiply(self, A):
        B = []
        for _ in range(len(A)):
            temp = 1
            for __ in range(len(A)):
                if _ != __ :
                    temp *= A[__]
            B.append(temp)
        return B

#别人的想法
# 画出一个矩阵
# B[0]:   1   A[1]   A[2] ...... A[n-1]
# B[1]: A[0]   1     A[2] ...... A[n-1]
# B[2]: A[0]  A[1]     1   ......A[n-1]
#可以看出 对于B[i]的值是矩阵中第I行的乘积 先把下三角乘起来
# （对于下三角 第一行为1 第二行为1*A[0] 第三行为第二行的积*A[1]
# 乘完之后再乘上三角
# （B[n-1]行为1，B[n-2]行为B[n-1]行的积*A[n-1] 依次类推 和暴力法相比 快3ms

class SolutionB:
    def multiply(self, A):
        B = []
        #先计算下三角
        B.append(1)
        for _ in range(1, len(A)):
            B.append(B[_-1] * A[_-1])
        print(B)
        #再计算上三角
        temp = 1
        for __ in range(len(A)-2, -1, -1):
            print(temp,B[__])
            temp = temp * A[__ + 1]
            B[__] = B[__] * temp
        return B

D = SolutionB()
print(D.multiply([1,2,3,4,5]))