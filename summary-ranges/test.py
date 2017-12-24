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
##     https://leetcode.com/problems/summary-ranges/description/
##    ,-----------
##    | Given a sorted integer array without duplicates, return the summary of its ranges.
##    | 
##    | Example 1:
##    | Input: [0,1,2,4,5,7]
##    | Output: ["0->2","4->5","7"]
##    | Example 2:
##    | Input: [0,2,3,4,6,8,9]
##    | Output: ["0","2->4","6","8->9"]
##    | Credits:
##    | Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
##    | 
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ## Basic Idea: 2 pointer
        ## Complexity: Time O(n), Space O(1)
        ## Assumptions:
        res = []
        length = len(nums)
        i=0
        while i<length:
            j = i + 1
            while j<length and nums[j] == nums[j-1] + 1:
                j += 1
            if j != i+1:
                res.append("%d->%d" % (nums[i], nums[j-1]))
            else:
                res.append("%d" % nums[i])
            i = j
        return res
