#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/sum-of-two-integers/description/
##    ,-----------
##    | Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
##    | 
##    | Example:
##    | Given a = 1 and b = 2, return 3.
##    | 
##    | Credits:
##    | Special thanks to @fujiaozhu for adding this problem and creating all test cases.
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:12>
##-------------------------------------------------------------------
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ## Idea: a xor b: get sum without carry. a & b >> 1 carry
        ## Complexity:
        ## Sample data:
        ##       9
        ##       5
        ##     8 4 2 1
        ##     1 0 0 1
        ##     0 1 0 1
        ##
        ## res 1 1 1 0
        ##
        ## or  1 1 0 1
        ## and 0 0 0 1
        ## xor 1 1 0 0
        ##
        ##     8 4 2 1
        ##     0 0 1 0
        ##     0 0 1 1
        ##
        ##     0 1 0 0
        ##     0 0 0 1
        MOD     = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b!= 0:
            c = a & b
            a = (a ^ b) & MOD
            b = (c << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT
