#https://leetcode.com/problems/word-break/


class Solution(object):
    def wordBreak(self, str, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        N = len(str)
        wordSet = set(wordDict)
        def canBreak(idx):
            if idx == N:
                return True
            for i in range(idx, N):
                word = str[idx:i+1]
                print(word)
                if word in wordSet and canBreak(i+1):
                    return True
            return False
        return canBreak(0)


class Solution(object):
    def wordBreak(self, str, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        N = len(str)
        wordSet = set(wordDict)
        memo = [-1]*N
        def canBreak(idx):
            if idx == N:
                return True
            if memo[idx] != -1:
                return memo[idx]
            for i in range(idx, N):
                word = str[idx:i+1]
                if word in wordSet and canBreak(i+1):
                    memo[idx] = True
                    return True
            memo[idx] = False
            return False
        
        return canBreak(0)

class Solution(object):
    def wordBreak(self, str, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        N = len(str)
        wordSet = set(wordDict)
        dp = [False]*(N+1) # dp[len] tells that staring from idx 0 of length len, whether it can be broken or not
        dp[0] = True
        for l in range(1, N+1):
            for i in range(l):
                if dp[i] and str[i:l] in wordSet:
                    dp[l] = True
                    break
        return dp[N]
        