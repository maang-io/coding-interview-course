#

# from right, using stack

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        N = len(heights)
        stack = list()
        result = list()
        for i in range(N-1, -1, -1):
            if stack and heights[stack[-1]] >= heights[i]:
                continue
            stack.append(i)
        while stack:
            result.append(stack.pop())
        return result

#from right, no stack
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        N = len(heights)
        result = list()
        result.append(N-1) # right most building will always have the view
        maxHeight = heights[N-1]
        for i in range(N-2, -1, -1):
            if heights[i] > maxHeight:
                result.append(i)
                maxHeight = heights[i]
        result.reverse()
        return result

# from left, using stack
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        N = len(heights)
        stack = list()
        for i in range(N):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack
    
"""
follow up, what if there are ocean on both sides
give the index of the building that have ocean view
both sides


"""
