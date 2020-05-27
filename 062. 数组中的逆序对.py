
#在数组中的两个数字，如果前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007


#使用归并排序进行统计 暴力法超时
#当A和B两个段进行比较时 如果A中的数a大于B中的数b， 那么a之后的数一定都大于b
class Solution:
    def __init__(self):
            self.count = 0
    def InversePairs(self, data):
        self.deep(data)
        return self.count % 1000000007
    def deep(self, data):
        if len(data) <= 1:
            return data
        mid = len(data)//2
        left = self.deep(data[:mid])
        right = self.deep(data[mid:])
        i =0
        j = 0
        result = []
        while i < len(left) and j<len(right):
            if left[i] > right[j]:
                result.append(right[j])
                self.count += (len(left) -i )
                j+=1
            else:
                result.append(left[i])
                i+=1
        result.extend(right[j:])
        result.extend(left[i:])
        return result

a = Solution()
print(a.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))