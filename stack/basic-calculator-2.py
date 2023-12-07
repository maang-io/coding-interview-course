
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        curNum, prevNum, result = 0,0,0
        prevSign = '+'
        s = s.replace(" ", "")
        N = len(s)
        for i in range(N):
            ch = s[i]
            if ch.isdigit():
                curNum = curNum*10 + int(ch)
            if not ch.isdigit() or i == N-1:
                if prevSign == '+':
                    result+= prevNum
                    prevNum = curNum
                elif prevSign == '-':
                    result+= prevNum
                    prevNum = -curNum
                elif prevSign == '*':
                    prevNum *= curNum
                elif prevSign == '/':                   
                    div = abs(prevNum)//curNum
                    prevNum = div if prevNum >= 0 else -div
                prevSign = s[i]
                curNum = 0
        result += prevNum
        return result
