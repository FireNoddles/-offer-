# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# stupid method 逐个查最小 on
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        i = rotateArray[0]
        for _ in rotateArray:
            if _ < i:
                i = _
        return i
#2. < On
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        i = rotateArray[0]
        for _ in range(len(rotateArray)-1):
            if rotateArray[_] > rotateArray[_ + 1]:
                return rotateArray[_ + 1]

#3. 折半查找 https://blog.nowcoder.net/n/dcb0f2e6ffd44e1895b7a5297e362778?f=comment
#注意停止的条件 和特殊情况1011111
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        i = 0
        j = len(rotateArray)-1
        mid = (i+j) // 2
        while i<j :
            if rotateArray[i]<rotateArray[j]:
                return rotateArray[i]
            if rotateArray[mid]>rotateArray[i]:
                i = mid+1
                mid = (i+j) // 2
            elif rotateArray[mid]<rotateArray[j]:
                j = mid
                mid = (i+j) // 2
            else:
                i+=1
        return rotateArray[i]
