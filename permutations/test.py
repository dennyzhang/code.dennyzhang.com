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
##     https://leetcode.com/problems/permutations/description/
##    ,-----------
##    | Given a collection of distinct numbers, return all possible permutations.
##    | 
##    | For example,
##    | [1,2,3] have the following permutations:
##    | [
##    |   [1,2,3],
##    |   [1,3,2],
##    |   [2,1,3],
##    |   [2,3,1],
##    |   [3,1,2],
##    |   [3,2,1]
##    | ]
##    `-----------
##
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## Idea:
        ## Complexity:
        length = len(nums)
        if length == 0:
            return []
        if length == 1:
            return [nums]
        res = []
        for i in xrange(length):
            l = self.permute(nums[:i]+nums[i+1:])
            for element in l:
                element = [nums[i]] + element
                res.append(element)
        return res