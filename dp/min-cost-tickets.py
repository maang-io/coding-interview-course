
import sys


class Solution_recursive(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        travelDates = set(days)
        def getCost(day):
            if day > days[-1]:
                return 0
            if day not in travelDates:
                return getCost(day+1)
            # 3 options to purchase
            # purchase 1 day pass
            cost1 = costs[0]+getCost(day+1)
            #purchase 7 day pass
            cost7 = costs[1] + getCost(day+7)
            #purchase 30 day pass
            cost30 = costs[2] + getCost(day+30)
            return min(min(cost1,cost7),cost30)
                    
        return getCost(1)

class Solution_recursive_window(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        daysN = len(days)
        validity = [1,7,30]
        def getCost(dayIdx):
            if dayIdx >= daysN:
                return 0
            
            result = sys.maxint
            # 3 options to purchase
            for i in range(3):
                nextDay = days[dayIdx]+validity[i]
                nextDayIdx = dayIdx
                while nextDayIdx < daysN and days[nextDayIdx] < nextDay:
                    nextDayIdx+=1
                result = min(result, costs[i]+getCost(nextDayIdx))
            
            return result
                    
        return getCost(0)
    
class Solution_memo(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        daysN = len(days)
        costN = 3
        validity = [1,7,30]
        travelDates = set(days)
        memo = [-1]*366

        def getCost(day):
            if day > days[-1]:
                return 0
            if day not in travelDates:
                return getCost(day+1)

            if memo[day] != -1:
                return memo[day]
            # 3 options to purchase

            # purchase 1 day pass
            cost1 = costs[0]+getCost(day+1)
            #purchase 7 day pass
            cost7 = costs[1] + getCost(day+7)
            #purchase 30 day pass
            cost30 = costs[2] + getCost(day+30)

            memo[day]= min(min(cost1,cost7),cost30)
            return memo[day]
                    

        return getCost(1)