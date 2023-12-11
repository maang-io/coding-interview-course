#https://leetcode.com/problems/longest-string-chain/description/
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # create a set for fast lookup
        # we would need to sort in decreasing order of word length
        # a recursive function that returns the length of the chain from the given word
        #   in this function we will remove one char at a time
        #   if the word is present in the set, you call the same recursive function

        wordSet = set(words)
        N = len(words)
       # sortedWords = sorted(words, key=lambda word:len(word), reverse=True)
        def getLongest(word):
            n = len(word)
            if n == 1:
                return 1  
            result = 1 # count the current word
            for i in range(n):
                nextWord = word[:i]+word[i+1:]
                if nextWord not in wordSet:
                    continue
                temp = getLongest(nextWord)
                result = max(temp+1,result)
            return result
        
        result = 0
        for word in words:
            temp = getLongest(word)
            result = max(temp, result)
        return result

"""
If we take a look at the previous solution,
we should notice that we are solving the same word multiple
times, so if we can cache that result we can solve in 
better time complexity
may be a dictionary <word,length> would work here
"""


class Solution_memo(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordSet = set(words)
        N = len(words)
        memo = dict()
        def getLongest(word):
            n = len(word)
            if n == 1:
                return 1  
            if word in memo:
                return memo[word]
            result = 1 # count the current word
            for i in range(n):
                nextWord = word[:i]+word[i+1:]
                if nextWord not in wordSet:
                    continue
                temp = getLongest(nextWord)
                result = max(temp+1,result)
            memo.update({word: result})
            return result
        
        result = 0
        for word in words:
            temp = getLongest(word)
            result = max(temp, result)
        return result

class Solution_dp(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordSet = set(words)
        N = len(words)
        # sort the words based on increasing order of the word  length
        sortedWords = sorted(words, key=lambda word:len(word), reverse=False)
        dp = dict()
        result = 0
        for word in sortedWords:
            n = len(word)
            curResult = 1 # by default the chain length is 1
            for i in range(n):
                nextWord = word[:i]+word[i+1:]
                if nextWord not in dp:
                    continue
                curResult = max(curResult, dp[nextWord]+1)
            if word in dp:
                dp.update({word:max(dp[word], curResult)})
            else:
                dp.update({word:curResult})
            result = max(result, dp[word])
        return result
