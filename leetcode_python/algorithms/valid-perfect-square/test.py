#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/valid-perfect-square/description/
##    ,-----------
##    | Given a positive integer num, write a function which returns True if num is a perfect square else False.
##    | 
##    | Note: Do not use any built-in library function such as sqrt.
##    | 
##    | Example 1:
##    | 
##    | Input: 16
##    | Returns: True
##    | Example 2:
##    | 
##    | Input: 14
##    | Returns: False
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-30 15:41:52>
##-------------------------------------------------------------------
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Idea: Binary search.
        ##       First compare num/2, then num/4 or num/2+num/4, ...
        ## Complexity: Time O(log2(n)), Space O(1)
        if num < 0:
            return False

        l,r = 0, num
        while l<r:
            mid = (l+r)/2
            if mid*mid > num:
                r = mid -1
            elif mid*mid < num:
                l = mid + 1
            else:
                return True
        return l*l == num
