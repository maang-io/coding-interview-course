class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        def canJumpHelper(idx): # returns true/false if we can reachat the end form idx
            if idx >= N-1:
                return True
            count = nums[idx]
            if count == 0:
                return False

            for i in range(1, count+1):
                if canJumpHelper(idx+i):
                    return True
            return False

        return canJumpHelper(0)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        memo = [-1]* N
        def canJumpHelper(idx): # returns true/false if we can reachat the end form idx
            if idx >= N-1:
                return True
            if memo[idx] != -1:
                return memo[idx] == 1
            count = nums[idx]
            if count == 0:
                memo[idx] = 0
                return False

            for i in range(1, count+1):
                if canJumpHelper(idx+i):
                    memo[idx] = 1
                    return True
            memo[idx] = 0
            return False

        return canJumpHelper(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        @cache
        def canJumpHelper(idx): # returns true/false if we can reachat the end form idx
            if idx >= N-1:
                return True
            count = nums[idx]
            if count == 0:
                return False

            for i in range(1, count+1):
                if canJumpHelper(idx+i):
                    return True
            return False

        return canJumpHelper(0)
        
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        dp = [0]*N
        dp[0] = True
        for i in range(N):
            if dp[i] == False or nums[i] == 0:
                continue            
            count = nums[i]
            j = count+1
            for j in range(1, count+1):
                idx = min(i+j, N-1)
                dp[idx] = True
        return dp[N-1]
    

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        N = len(nums)
        for i in range(N):
            if reach < i:
                return False
            reach = max(reach, i+nums[i])
        return True