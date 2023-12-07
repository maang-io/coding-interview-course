# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenDict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for c in s :
            if c in parenDict: # got the closing paren
                if len(stack) == 0:
                    return False
                topC = stack.pop()
                if topC != parenDict[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        