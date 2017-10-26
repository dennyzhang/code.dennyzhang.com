#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/climbing-stairs/description/
##    ,-----------
##    | You are climbing a stair case. It takes n steps to reach to the top.
##    | 
##    | Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
##    | 
##    | Note: Given n will be a positive integer.
##    `-----------
##
## Tags: #redo
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    ## Idea: fibonacci
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Idea: DP
        ## Complexity: Time ? , Space ?
        if n == 1:
            return 1
        if n == 2:
            return 2
        value1 = 1
        value2 = 2
        for i in range(3, n):
            value = value2
            value2 = value1 + value2
            value1 = value
        return value1 + value2
