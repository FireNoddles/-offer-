#请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。



#两个栈实现
class Solution:
    def Print(self, pRoot):
        stack1 = []
        stack2 = []
        result = []
        if pRoot == None:
            return []
        stack1.append(pRoot)
        layer = 1
        while len(stack1)!=0 or len(stack2)!=0:
            if layer % 2 != 0:
                layertemp = []
                while len(stack1)!=0:
                    temp = stack1.pop()
                    layertemp.append(temp.val)
                    if temp.left!=None:
                        stack2.append(temp.left)
                    if temp.right!=None:
                        stack2.append(temp.right)
                layer+=1
                if len(layertemp)!=0:
                    result.append(layertemp)
            else:
                layertemp = []
                while len(stack2)!=0:
                    temp = stack2.pop()
                    layertemp.append(temp.val)
                    if temp.right != None:
                        stack1.append(temp.right)
                    if temp.left!= None:
                        stack1.append(temp.left)
                layer+=1
                if len(layertemp)!=0:
                    result.append(layertemp)
        return result