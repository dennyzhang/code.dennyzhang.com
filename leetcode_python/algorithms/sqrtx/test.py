#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/sqrtx/description/
##    ,-----------
##    | Implement int sqrt(int x).
##    | 
##    | Compute and return the square root of x.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-01 18:36:12>
##-------------------------------------------------------------------
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ## Idea: First check x/2, then x/4 or x/2 + x/4, then ...
        ## Complexity: Time O(log2(n)), Space O(1)
        ## Sample Data:
        ##      100
        ##    6 12 25 50
        if x < 0:
            raise Exception("Invalid input. x:%d" %(x))
        l,r = 0, x

        while l<r:
            v = (r+l)/2
            if v*v > x:
                r = v - 1
            elif v*v < x:
                l = v + 1
            else:
                return v

        return l-1 if l*l > x else l
