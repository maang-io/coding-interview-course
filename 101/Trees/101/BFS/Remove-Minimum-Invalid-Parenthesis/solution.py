#https://leetcode.com/problems/remove-invalid-parentheses/description/

"""
Thoughts:
we can traverse the string skipping any chars which are not ( or )
when we encounter any ( ), we have 2 options
1. keep the paren, and move to next
2. delete the paren, and then move to next
and then check if the remaining is valid or not

and this can be done for each ( ), so if length of the strings are N, then
overall time complexity of this soltuion would be 2^N
not a great solution, let us see if we can find a better approach

since we have to find minimum number of chars to be removed, may be bfs can help
so if we have to remove 1 chars, we can remove all of them and one by one,
and check if we have a valid paren, if we found a valid paren, this will be minimum number of chars removed


"""

class Solution(object):
    def removeInvalidParentheses(self, str):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(str):
            count = 0
            for c in str:
                if count < 0:
                    return False
                if c == '(':
                    count+=1
                elif c == ')':
                    count-=1
            return count == 0
            
        q = deque([str])
        result = list()
        visited = set()
        while len(q) > 0:
            qsz = len(q)
            for _ in range(qsz):
                cur = q.popleft()
                #check for validation
                valid = isValid(cur)
                if valid:
                    result.append(cur)
                # since we have found the min, there is no meaning to add new chars, 
                # we just need to handle all the items present in the queue
                if len(result)>0:
                    continue
                # explore the options
                for i in range(len(cur)):
                    if cur[i] != '(' and cur[i] != ')':
                        continue
                    next = cur[:i]+cur[i+1:]
                    if next in visited:
                        continue
                    q.append(next)
                    visited.add(next)
        return result