class Solution_burteForce(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        N = len(t)
        result = [0]*N
        for i in range(N):
            for j in range(i,N):
                if t[j] > t[i]:
                    result[i] = j-i
                    break
        return result
        
class Solution(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        N = len(t)
        result = [0]*N
        stack = []
        for i in range(N):
            while stack and t[stack[-1]] < t[i]:
                popIdx = stack.pop()
                result[popIdx] = i-popIdx 
            stack.append(i)
        return result
        