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
##     https://leetcode.com/problems/find-peak-element/description/
##    ,-----------
##    | A peak element is an element that is greater than its neighbors.
##    | 
##    | Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
##    | 
##    | The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
##    | 
##    | You may imagine that num[-1] = num[n] = -∞.
##    | 
##    | For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
##    | 
##    | click to show spoilers.
##    | 
##    | Credits:
##    | Special thanks to @ts for adding this problem and creating all test cases.
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0
        if length == 0:
            return -1

        for i in range(1, length-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        if nums[0] > nums[1]:
            return 0
        if nums[length-1] > nums[length-2]:
            return length-1
        return -1
