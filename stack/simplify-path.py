#https://leetcode.com/problems/simplify-path/description/
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split('/')
        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack :
                    stack.pop()
            else:
                stack.append(part)
        
        result = '/'.join(stack)
        return '/'+result
        