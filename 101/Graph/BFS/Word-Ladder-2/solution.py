#https://leetcode.com/problems/word-ladder-ii/

'''
Thoughts:
shortest transformation sequence => BFS

hit, every char can be replaced by (a,z), total 3^26 combination
for each combination, check if the word is in the dictionary
and then add it to the queue.

every entity in the queue, shoukd contains 2 things
1. the current word
2. the path, how this word has been build
'''

from collections import deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # setup
        wordSet = set(wordList)
        alphabets = "abcdefghijklmnopqrestuvwxyz"
        result = list([])
        q = deque([beginWord, list(beginWord)]) # queue contains tuple
        visited = set([beginWord])

        def explore(cur, curPath) :
            N = len(cur)
            for i in range(N):
                # for ith char
                for c in alphabets:
                    next =  + cur[:i]+ str(c) + cur[i+1:]
                    print(next)
                    if next not in wordSet:
                        continue
                    if next in visited:
                        continue
                    q.append([next, curPath.add(next)])
                    if next != endWord:
                        visited.add(next)
                    

        
        # while we have items in the queue
        while len(q) > 0:
            qsz = len(q)
            # pop all items one by one at the current level
            for _ in range(qsz):
                cur, curPath = q.popleft()
                if cur == endWord:
                    result.append(curPath)

                if len(result) > 0:
                    continue

                explore()            

        # for cur word

        # if it is an end word, put it in the result

        # if we have not found any result we might want to explore the next words

        # build the next set of words , 
        #   by replacing each char, an
        #   if is in dict, add it to queue