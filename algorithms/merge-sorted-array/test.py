#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description :
##     https://leetcode.com/problems/merge-sorted-array/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-22 15:32:27>
##-------------------------------------------------------------------
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 
        j = n - 1
        index = m + n -1

        while(i >= 0 and j >= 0):
            # print("nums1[i]: %d, nums2[j]: %d, index: %d" % (nums1[i], nums2[j], index))
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
                index -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
                index -= 1

        if i< 0:
            while(j>=0):
                nums1[index] = nums2[j]
                j -= 1
                index -= 1
                
if __name__ == '__main__':
    s = Solution()
    l1 = [0] * 7
    l1[0] = 1
    l1[1] = 2
    l1[2] = 5
    s.merge(l1, 3, [2, 2, 4, 6], 4)
    # print l1

    l1 = [0] * 1
    l1[0] = 1
    s.merge(l1, 1, [], 0)
    # print l1

    l1 = [0] * 2
    l1[0] = 0
    s.merge(l1, 0, [1], 1)
    #print l1    
## File: test.py ends
