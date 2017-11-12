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
##     https://leetcode.com/problems/intersection-of-two-arrays/description/
##    ,-----------
##    | Given two arrays, write a function to compute their intersection.
##    | 
##    | Example:
##    | Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
##    | 
##    | Note:
##    | Each element in the result must be unique.
##    | The result can be in any order.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ## Use map
        dict_num = {}
        l = []
        for num in nums1:
            if dict_num.has_key(num) is False:
                dict_num[num] = (1, 0)
        for num in nums2:
            if dict_num.has_key(num) is True:
                dict_num[num] = (1, 1)
        for num in dict_num.keys():
            (_in_nums1, in_nums2) = dict_num[num]
            if in_nums2 == 1:
                l.append(num)
        return l
        
    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ## use set
        return list(set(nums1).intersection(set(nums2)))

    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ## Ideas: sort 2 lists, then merge them
        ## Complexity: Time O(n*log(n)), Space O(n)
        ## Sample Data
        ##     1 1 2 2
        ##         2 2
        l1 = sorted(nums1)
        l2 = sorted(nums2)
        l = []
        i = 0
        j = 0
        k = -1
        while (i<len(nums1) and j<len(nums2)):
            if l1[i] < l2[j]:
                i += 1
            elif l1[i] > l2[j]:
                j += 1
            else:
                if k == -1:
                    l.append(l1[i])
                    k += 1
                else:
                    if l[k] != l1[i]:
                        l.append(l1[i])
                        k += 1
                i += 1
                j += 1
        return l
