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
##     https://leetcode.com/problems/3sum-closest/description/
##    ,-----------
##    | Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
##    | 
##    |     For example, given array S = {-1 2 1 -4}, and target = 1.
##    | 
##    |     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-30 15:41:52>
##-------------------------------------------------------------------
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## Idea: sort the list. target_sum, 3 indices: i, l, r
        ## Complexity:
        ## Sample Data
        nums.sort()
        if len(nums) < 3:
            return None
        res = nums[0] + nums[1] + nums[2]
        for i in xrange(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                value = nums[i] + nums[l] + nums[r]
                offset = abs(value - target)
                if value == target:
                    return value

                if abs(res - target) > offset:
                    res = value

                if value > target:
                    r -= 1
                if value < target:
                    l += 1
        return res

    def threeSumClosest_v1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## Idea: sort the list. target_sum, 3 indices: i, l, r
        ## Complexity:
        ## Sample Data
        nums.sort()
        res = None
        for i in xrange(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                value = nums[i] + nums[l] + nums[r]
                offset = abs(value - target)
                if res is None:
                    res = value
                if abs(res - target) > offset:
                    res = value

                if value > target:
                    r -= 1
                elif value < target:
                    l += 1
                else:
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
