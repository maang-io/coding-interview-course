#https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution1(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def getCost(i): # retruns the total cost to reach at ith pos
            if i == 0 or i == 1:
                return 0
            cost1 = getCost(i-1)+cost[i-1]
            cost2 = getCost(i-2)+cost[i-2]
            return min(cost1,cost2)
        
        return getCost(len(cost))
    
class Solution2(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        memo = [-1]*(N+1)
        def getCost(idx):
            if idx == 0 or idx == 1:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            cost1 = getCost(idx-1)+cost[idx-1]
            cost2 = getCost(idx-2)+cost[idx-2]
            memo[idx] = min(cost1,cost2)
            return memo[idx]
        
        return getCost(len(cost))
    

class Solution3(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        dp = [0]*(N+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, N+1):
            dp[i] = min(dp[i-2]+ cost[i-2],
                        dp[i-1]+ cost[i-1])
        return dp[N]