# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

# 注意处理边界
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix == None:
            return []
        result = []
        up = 0
        down = len(matrix)
        left = 0
        right = len(matrix[0])
        while 1:
            for _ in range(left, right):
                result.append(matrix[up][_])
            up+=1
            if up > down or len(result) == (len(matrix[0])*len(matrix)):
                break
            for _ in range(up, down):
                result.append(matrix[_][right-1])
            right-=1
            if right < left or len(result) == (len(matrix[0])*len(matrix)):
                break
            for _ in range(right, left, -1):
                result.append(matrix[down-1][_-1])
            down -= 1
            if down < up or len(result) == (len(matrix[0])*len(matrix)):
                break
            for _ in range(down, up, -1):
                result.append(matrix[_-1][left])
            left += 1
            if left > right or len(result) == (len(matrix[0])*len(matrix)):
                break
        return result
        # write code here
