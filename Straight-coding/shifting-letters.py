#https://leetcode.com/problems/shifting-letters/description/

class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        N = len(s)
        result = [' ']*N
        result = [char for char in s]
        for i in range(N-1, -1, -1):
            if i+1 < N:
                shifts[i] += shifts[i+1]
            ascii_code = ord(s[i])
            shift_count = shifts[i]%26
            result[i] = chr(ascii_code+shift_count)
        return ''.join(result)
    
# follow up: what if you are not allowed to modify shifts array or allocate the new array
    
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        N = len(s)
        result = [' ']*N
        result = [char for char in s]
        shift_count = 0
        for i in range(N-1, -1, -1):
            shift_count += shifts[i]
            ascii_code = ord(s[i])-ord('a')+shift_count
            result[i] = chr(ascii_code%26+ord('a'))
        return ''.join(result)