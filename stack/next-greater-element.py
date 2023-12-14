#https://leetcode.com/problems/next-greater-element-i/description/
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        N1 = len(nums1)
        N2 = len(nums2)
        result = [-1]*N1
        for i in range(N1):
            found = False
            for j in range(N2):
                if found and nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    break
                if nums2[j] == nums1[i] and found == False:
                    found = True
        return result


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        N1 = len(nums1)
        N2 = len(nums2)
        positions = dict()
        result = [-1]*N1
        for i in range(N2):
            positions.update({nums2[i]: i})
        for i in range(N1):
            pos = positions[nums1[i]]
            for j in range(pos+1, N2):
                if nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    break
        return result

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        N1 = len(nums1)
        positions = dict()
        result = [-1]*N1
        stack = list()

        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                positions.update({prev:num})
            stack.append(num)
        for i in range(N1):
            if nums1[i] in positions:
                result[i] = positions[nums1[i]]
        return result