#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: ##brain
## Description:
##     https://leetcode.com/problems/permutations-ii/description/
##    ,-----------
##    | Given a collection of numbers that might contain duplicates, return all possible unique permutations.
##    | 
##    | For example,
##    | [1,1,2] have the following unique permutations:
##    | [
##    |   [1,1,2],
##    |   [1,2,1],
##    |   [2,1,1]
##    | ]
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self._permuteUnique(nums)

    def _permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0:
            return []
        if length == 1:
            return [nums]
        res = []
        for i in xrange(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = self._permuteUnique(nums[:i] + nums[i+1:])
            for element in l:
                element = [nums[i]] + element
                res.append(element)
        return res
