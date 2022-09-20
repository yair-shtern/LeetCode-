# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        h = total // 2
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = h - i - 2

            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Aleft = A[i] if i >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (min(Aright, Bright) + max(Aleft, Bleft)) / 2.0
            else:
                if Aleft > Bright:
                    r = i - 1
                else:
                    l = i + 1