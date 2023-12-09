#https://leetcode.com/problems/coin-change-ii/submissions/

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins = sorted(coins)
        N = len(coins)
        def change(idx, amount):
            if amount == 0:
                return 1
            if idx >= N:
                return 0
           
            if amount < coins[idx]:
               return 0

            count = 0
            # option 1 do not take coins[idx]
            count += change(idx+1, amount)

            # option 2, take coins[idx]
            count += change(idx, amount-coins[idx])
            return count
        
        return change(0, amount)