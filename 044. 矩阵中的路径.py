# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 \begin

# 矩阵中包含一条字符串
# "bcced"
# 的路径，但是矩阵中不包含
# "abcb"
# 路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。


# 方法1 未知错误
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols + j] == path[0] and self.find(list(matrix), i,j,rows, cols, path[1:]):
                    return True
        return False
    def find(self, matrix, i,j, rows, cols, path):
        if not path:
            return True
        matrix[i*cols + j] = '0'
        if j+1 < cols and matrix[i*cols + j+1] == path[0] and self.find(matrix, i ,j+1,rows, cols, path[1:]):
            return True
        if j-1 >= 0 and matrix[i*cols + j-1] == path[0] and self.find(matrix, i ,j-1,rows, cols, path[1:]):
            return True
        if i+1<rows and matrix[(i+1)*cols + j] == path[0] and self.find(matrix, i+1 ,j,rows, cols, path[1:]):
            return True
        if i-1 >= 0 and matrix[(i-1)*cols + j]== path[0] and self.find(matrix, i-1 ,j,rows, cols, path[1:]):
            return True
        matrix[i * cols + j] = path[0]
        return False


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        visited = [0 for i in range(len(matrix))]
        for i in range(rows):
            for j in range(cols):
                if self.find(list(matrix), i,j,rows, cols, path):
                    return True
        return False
    def find(self, matrix, i, j, rows, cols, path):
        if matrix[i*cols + j] == path[0]:
            matrix[i*cols + j] = ''
            if len(path) == 1:
                return True
            if i > 0 and self.find(matrix, i-1, j, rows, cols, path[1:]):
                return True
            if i<rows-1 and self.find(matrix, i+1, j, rows, cols, path[1:]):
                return True
            if j > 0 and self.find(matrix, i, j-1, rows, cols, path[1:]):
                return True
            if j<cols-1 and self.find(matrix, i, j+1, rows, cols, path[1:]):
                return True
            matrix[i*cols + j] = path[0]
            return False
        else:
            return False
        # write code here

# AB---JIG
# SF---OPQ
# AD-EMNOE
# AD--EJFM
# VCEIFGGS
# ABCEHJIG
# SFCSLOPQ
# ADEEMNOE
# ADIDEJFM
# VCEIFGGS