# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#空间差 On
class Solution:
    def reOrderArray(self, array):
        add= []
        dou = []
        for _ in array:
            if _ % 2 == 0:
                dou.append(_)
            else:
                add.append(_)
        add.extend(dou) # 不能直接return它
        return add


# On2思路
#i++往前走碰到偶数停下来，j = i+1
# 若 a[j]为偶数，j++前进，直到碰到奇数
# a[j]对应的奇数插到a[i]位置，j经过的j-i个偶数依次后移
# 如果j==len-1时还没碰到奇数，证明i和j之间都为偶数了，完成整个移动

#复杂度高 但省空间 c代码
#class Solution {
# public:
#     void reOrderArray(vector<int> &array) {
#         int len = array.size();
#         if(len <= 1){ // 数组空或长度为1
#             return;
#         }
#
#         int i = 0;
#         while(i < len){
#             int j = i + 1;
#             if(array[i]%2 == 0){ // a[i]为偶数，j前进，直到替换
#                 while(array[j]%2 == 0){ // j为偶数，前进
#                     if(j==len-1)// i为偶数，j也为偶数，一直后移到了末尾，证明后面都是偶数
#                          return;
#                     j++;
#                 }
#                 // 此时j为奇数
#                 int count = j-i;
#                 int temp = array[i];
#                 array[i] = array[j];
#                 while(count>1){
#                     array[i+count] = array[i+count-1];//数组后移
#                     count--;
#                 }
#                 array[i+1] = temp;
#             }
#             i++;
#         }
#     }
# };