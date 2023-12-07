#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = ["+","-","*","/"]
        def eval2(oprnd1, oprnd2, ops):
            if ops == "+":
                return int(oprnd1)+int(oprnd2)
            elif ops == "-":
                return int(oprnd1)-int(oprnd2)
            elif ops == "*":
                return int(oprnd1)*int(oprnd2)
            elif ops == "/":
                return int(float(oprnd1)/float(oprnd2))
            
        for token in tokens:
            if token in ops :
                opr2 = stack.pop()
                opr1 = stack.pop()
                temp = eval2(opr1,opr2,token)

                stack.append(str(temp))
            else:
                stack.append(token)
        
        return int(stack.pop())
