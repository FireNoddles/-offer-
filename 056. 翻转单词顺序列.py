#牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
# 同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，
# 但却读不懂它的意思。例如，“student. a am I”。后来才意识到，
# 这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
# Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？


# 先切分 在拼接
class Solution:
    def ReverseSentence(self, s):
        re = []
        # temp = ''
        # for _ in range(len(s)):
        #     if s[_] != ' ':
        #         temp += s[_]
        #     elif s[_] == ' ':
        #         re.insert(0, temp)
        #         temp = ''
        # re.insert(0, temp)
        # temp= ''
        l = s.split(' ')
        temp = ''
        for _ in range(len(l)-1,-1,-1):
            if _!= 0:
                temp += l[_]+' '
            else:
                temp +=  l[_]
        print(temp)

a = Solution()
a.ReverseSentence('i am a student.')