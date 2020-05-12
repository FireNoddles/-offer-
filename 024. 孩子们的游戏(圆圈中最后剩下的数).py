#每年六一儿童节,
# 牛客都会准备一些小礼物去看望孤儿院的小朋友,
# 今年亦是如此。HF作为牛客的资深元老,
# 自然也准备了一些小游戏。其中,有个游戏是这样的:
# 首先,让小朋友们围成一个大圈。
# 然后,他随机指定一个数m,让编号为0的小朋友开始报数。
# 每次喊到m-1的那个小朋友要出列唱首歌,
# 然后可以在礼品箱中任意的挑选礼物,
# 并且不再回到圈中,从他的下一个小朋友开始,
# 继续0...m-1报数....这样下去....
# 直到剩下最后一个小朋友,可以不用表演,
# 并且拿到牛客名贵的“名侦探柯南”典藏版
# (名额有限哦!!^_^)。请你试着想下,
# 哪个小朋友会得到这份礼品呢？
# (注：小朋友的编号是从0到n-1)
#如果没有小朋友，请返回-1

# 超时 思路 直接删除指定位置 把位置后面的数提到前面去 重新开始
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 2:
            return -1
        arr = [i for i in range(n)]
        while len(arr)>1:
            if m<=len(arr):
                del arr[m-1]
                i = 0
                for _ in range(m-1, len(arr)):
                    temp = arr[_]
                    del arr[_]
                    arr.insert(i, temp)
                    i+=1
            else:
                del arr[(m%len(arr))-1]
                i = 0
                for __ in range((m%len(arr))-1, len(arr)):
                    temp = arr[__]
                    del arr[__]
                    arr.insert(i, temp)
                    i+=1
        return arr[0]


# 当前位置 加上它上轮走过的个数 再除长度

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 2:
            return -1
        arr = [i for i in range(n)]
        i = 0
        while len(arr)>1:
            i = (m + i -1) % len(arr)
            del arr[i]
        return arr[0]