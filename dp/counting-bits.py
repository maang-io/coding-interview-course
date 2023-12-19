class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for num in range(0,n+1):
            result.append(self.bitcount(num))
        return result
    
    def bitcount(self, num) :
        count = 0
        while num != 0 :
            num = num & num-1
            count +=1
        return count 
        

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def countBits(num):
            count = 0
            while num > 0:
                num = num & num-1 ########optimized
                count+=1
            return count
          
        result = [0]*(n+1)
        for i in range(n+1):
            result[i] = countBits(i)
        
        return result

"""
if we take a look at the last apporach
num = num & num-1
count+=1
that means if we can find the number of bits in num&num-1
then number of bits for num = 1 + that value
"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """        
        result = [0]*(n+1)
        for i in range(1,n+1):          
            result[i] = result[i&(i-1)] + 1
        
        return result