#https://leetcode.com/problems/rotated-digits/


class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        flipMap = {
            1: 1,
            2: 5,
            5: 2,
            6: 9,
            8: 8,
            9: 6
        }
        def isGood(num):
            reversed = 0
            flipped = 0
            while num > 0:
                digit = num%10
                if digit not in flipMap:
                    return False
                flipped = flipped*10 +flipMap[digit]
                reversed = reversed*10+digit
                num = num//10
            return flipped != reversed
        
        result = 0
        for i in range(0,n+1):
            if isGood(i):
                result+=1
        return result


class Solution2(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        flags = [0]*(n+1)
        result = 0
        for i in range(0,n+1):
            if i == 0 or i == 1 or i == 8 :
                flags[i] = 1
            elif i == 2 or i == 5 or i == 6 or i == 9:
                flags[i] = 2
                result+=1
            else :
                a = flags[i//10]
                b = flags[i%10]
                if ( a == 1 and b == 1):
                    flags[i] = 1
                elif (a >= 1 and b >= 1):
                    flags[i] = 2
                    result +=1
                
        return result
    

class Solution3(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for num in range(1,n+1):
            num_str = str(num)
            if '3' in num_str or '4' in num_str or '7' in num_str:
                continue
            if '2' in num_str or '5' in num_str or '6' in num_str or '9' in num_str:
                result+=1

        return result
