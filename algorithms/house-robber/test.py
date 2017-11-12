#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #amusing, #redo
## Description:
##     https://leetcode.com/problems/house-robber/description/
##    ,-----------
##    | You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
##    | 
##    | Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
##    | 
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Idea: Recursive way will timeout
        ##       DP: robs[i] the max profit so far.
        ##       How does DP formula work?
        ## Complexity:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])

        robs = [None]*length
        robs[0] = nums[0]
        robs[1] = max(nums[0], nums[1])
        robs[2] = max(nums[0]+nums[2], nums[1])

        for i in range(3, length):
            robs[i] = max(robs[i-3]+nums[i-1], robs[i-2]+nums[i])
        return robs[-1]