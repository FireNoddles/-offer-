# 在一个二维数组中（每个一维数组的长度相同），
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。


# 从左上角开始找 比目标大 左移 比目标小 下移
class Solution:
    # array 二维列表
    def Find(self, target, array):
        i = 0
        j = len(array[0])-1
        while 1:
            if j < 0 or i>len(array)-1:
                return False
            else:
                if array[i][j] == target:
                    return True
                elif array[i][j] > target:
                    j = j-1
                elif array[i][j] < target:
                    i = i + 1