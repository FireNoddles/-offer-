#求1+2+3+...+n，
# 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


#不会 思路 用递归 解决for循环 再用 短路与 解决if
#python里的短路直接就是短路的 不分（短路与）和 （逻辑与） 下面为二者介绍
# & & （短路与）和 &（逻辑与）的时候：
#
# 有假则为假，全真则为真（有假必假，全真为真）
#
# | | （短路或）和 |（逻辑或）的时候：
#
# 有真则为真，全假则为假（有真必真，全假为假）
#
#
#
#
#
# 逻辑与和短路与的区别：逻辑与的判断方式是：
#
# 从左到右依次判断，直到结尾（逻辑全程运算）
#
#
#
#
#
# 短路与的判断方式是:
#
# 从左到右依次判断，直到出现false为止将不再判断，直接得到结果为false（短路遇false就停）
#
#
#
# 逻辑或和短路或的区别
# 逻辑或的判断方式是：
#
# 从左到右依次判断，直到结尾
#
# 短路或的判断方式是:
#
# 从左到右依次判断，直到出现true为止将不再判断，直接得到结果为true
class Solution:
    def Sum_Solution(self, n):
            result = n and n + self.Sum_Solution(n-1)
            return result