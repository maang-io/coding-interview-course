class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        stack.append(-1) # works like a tombstone
        N = len(s)
        result = 0
        for i in range(N):
            if s[i] == ')' and len(stack)>1 and s[stack[-1]] == '(':
                stack.pop()
                result = max(result, i- stack[-1])
            else:
                stack.append(i)
        return result

        
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        N = len(s)
        left = 0
        dp = [0]*N
        for i in range (N):
          if s[i] == '(':
            left+=1
          elif left > 0:
            dp[i] = dp[i-1]+2
            curLen = dp[i]
            if i >= curLen :
              dp[i] += dp[i-curLen]
            result = max(result,dp[i])
            left-=1
        return result
