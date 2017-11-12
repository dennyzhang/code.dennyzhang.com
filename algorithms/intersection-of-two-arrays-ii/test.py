#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
##    ,-----------
##    | Given two arrays, write a function to compute their intersection.
##    | 
##    | Example:
##    | Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
##    | 
##    | Note:
##    | Each element in the result should appear as many times as it shows in both arrays.
##    | The result can be in any order.
##    | Follow up:
##    | What if the given array is already sorted? How would you optimize your algorithm?
##    | What if nums1's size is small compared to nums2's size? Which algorithm is better?
##    | What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ## Sample data
        ##  1, 1, 2, 2
        ##        2, 2
        l1 = sorted(nums1)
        l2 = sorted(nums2)
        l = []
        i = 0
        j = 0
        while(i<len(nums1) and j<len(nums2)):
            if (l1[i] < l2[j]):
                i += 1
            else:
                if (l1[i] > l2[j]):
                    j += 1
                else:
                    l.append(l1[i])
                    i += 1
                    j += 1
        return l
