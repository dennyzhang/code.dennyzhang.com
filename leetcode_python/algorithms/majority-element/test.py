#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: amusing, #brain
## Description:
##     https://leetcode.com/problems/majority-element/description/
##    ,-----------
##    | Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
##    | 
##    | You may assume that the array is non-empty and the majority element always exist in the array.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-09 08:45:28>
##-------------------------------------------------------------------
class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Ideas: sort, then find the middle item
        ## Complexity: Time O(n*log(n)), Space O(1)
        length = len(nums)
        nums2 = sorted(nums)
        return nums2[(length-1)/2]
