# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
# 请问该机器人能够达到多少个格子？

class Solution:
    def __init__(self):
        self.result = []
    def movingCount(self, threshold, rows, cols):
        i = 0
        j = 0
        self.result = [0] * (rows*cols)
        self.digui(threshold, rows, cols,i ,j)
        return sum(self.result)
    def digui(self, threshold, rows, cols,i ,j):
        print(i*cols + j, rows*cols)

        if self.su(i, j) > threshold or self.result[i*cols + j] == 1:
            return 0
        else:
            self.result[i*cols + j] = 1
            if i > 0:
                self.digui(threshold, rows, cols, i-1 ,j)
            if i < rows-1:
                self.digui(threshold, rows, cols, i+1 ,j)
            if j < cols-1:
                self.digui(threshold, rows, cols, i ,j+1)
            if j > 0:
                self.digui(threshold, rows, cols, i ,j-1)
            return 0
    def su(self, i, j):
        re = 0
        for _ in str(i):
            re += int(_)
        for __ in str(j):
            re += int(__)
        return re
