#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/median-of-two-sorted-arrays/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:59:17>
##-------------------------------------------------------------------
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ## Basic Idea: merge 2 sorted array to one, find 2 values
        ## Complexity: O(m+n)
        m = len(nums1)
        n = len(nums2)
        nums3 = [0] * (m+n)
        i = 0
        j = 0
        k = 0
        while i<m and j<n:
            if nums1[i] <nums2[j]:
                nums3[k] = nums1[i]
                k += 1
                i += 1
            else:
                nums3[k] = nums2[j]
                k += 1
                j += 1

        while i<m:
            nums3[k] = nums1[i]
            k += 1
            i += 1

        while j<n:
            nums3[k] = nums2[j]
            k += 1
            j += 1

        ret = -1
        if (m+n)%2 == 1:
            ret = float(nums3[(m+n-1)/2])
        else:
            ret = float(nums3[(m+n)/2-1] + nums3[(m+n)/2])/2
        return ret
                
if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1, 3], [2])
    print s.findMedianSortedArrays([1, 2], [3, 4])
## File: test.py ends
