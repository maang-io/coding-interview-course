#https://leetcode.com/problems/basic-calculator/description/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        num = 0
        sign = 1
        N = len(s)
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == '+' or ch == '-':
                result += num*sign
                sign = 1 if ch == '+' else -1
                num = 0
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch== ')':
                result += sign*num
                result *= stack.pop()
                result += stack.pop()
                num = 0
        result += sign*num
        return result 