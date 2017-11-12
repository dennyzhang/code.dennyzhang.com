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
##     https://leetcode.com/problems/power-of-three/description/
##    ,-----------
##    | Given an integer, write a function to determine if it is a power of three.
##    | 
##    | Follow up:
##    | Could you do it without using any loop / recursion?
##    | 
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 21:40:38>
##-------------------------------------------------------------------
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ## Idea: loop
        ## Complexity: Time O(log3(n)) Space O(1)
        ##   3
        ##   9 = 3*3
        ##   27

        if n == 0:
            return False
        while (n % 3 == 0):
            n=n/3
        return n == 1
