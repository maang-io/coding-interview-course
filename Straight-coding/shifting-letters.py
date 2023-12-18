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