#HZ偶尔会拿些专业问题来忽悠那些
# 非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
# 并期望旁边的正数会弥补它呢？
# 例如:{6,-3,-2,7,-15,1,2,2},
# 连续子向量的最大和为8(从第0个开
# 始,到第3个为止)。给一个数组，
# 返回它的最大连续子序列的和，
# 你会不会被他忽悠住？
# (子向量的长度至少是1)

# 使用一个temp依次加和 若和变成负数 则从当前位置重新开始
# 若当前数为正 temp+它一定变大 记录最大 返回

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        tempsum = array[0]
        maxsum = array[0]
        for _ in range(1, len(array)):
            if tempsum < 0:
                tempsum = array[_]
            else:
                tempsum = tempsum + array[_]
            maxsum = tempsum if tempsum > maxsum else maxsum

        return maxsum