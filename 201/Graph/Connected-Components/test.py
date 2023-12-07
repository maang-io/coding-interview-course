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



def findLadders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    # setup
    result = list()
    if beginWord is None or endWord is None:
        return result
    wordSet = set(wordList)
    q = deque()
    tup = (beginWord,[beginWord])
    q.append(tup)
    visitedSet = set([beginWord])
    if endWord == beginWord or endWord not in wordSet:
        return result

    # get next options
    def getNextOptions(cur):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        nextOptions = list()
        N = len(cur)
        for i in range(N):
            for c in alphabets:
                next = cur[:i]+c+cur[i+1:]
                #print(next)
                if next not in wordSet or next == cur:
                    continue
                nextOptions.append(next)
        return nextOptions

    # do a bfs
    while len(q) > 0:
        qsz = len(q)
        for _ in range(0,qsz):
            print(len(q))
            (cur,curPath) = q.popleft()
            if cur == endWord:
                result.append(curPath)
            if len(result) > 0:
                continue

            nextOptions = getNextOptions(cur)
            for nextWord in nextOptions:
                if nextWord in visitedSet:
                    continue
                nextPath = list(curPath)
                nextPath.append(nextWord)
                q.append((nextWord, nextPath))
                if nextWord != endWord:
                    visitedSet.add(nextWord)

    return result

result = findLadders("a", "c", ["a","b","c"])
print(result)