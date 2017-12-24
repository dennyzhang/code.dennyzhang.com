#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/maximum-subarray/description/
##    ,-----------
##    | Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
##    | 
##    | For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
##    | the contiguous subarray [4,-1,2,1] has the largest sum = 6.
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 16:12:45>
##-------------------------------------------------------------------
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Idea:
        ## Complexity:
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return nums[0]
        # TODO
