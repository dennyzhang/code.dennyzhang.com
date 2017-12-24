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
##     https://leetcode.com/problems/sum-of-square-numbers/description/
##    ,-----------
##    | Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
##    | 
##    | Example 1:
##    | Input: 5
##    | Output: True
##    | Explanation: 1 * 1 + 2 * 2 = 5
##    | Example 2:
##    | Input: 3
##    | Output: False
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        ## Idea: a = 1, 2, 3, ...
        ## Complexity: Time O(log2(n)*log2(n)), Space O(1)
        import math
        a = 0
        while (a*a <= c):
            v = c-a*a
            # Python check whether it's square
            if int(v**.5)**2 == v:
                return True
            a += 1
        return False

    def judgeSquareSum1(self, c):
        """
        :type c: int
        :rtype: bool
        """
        ## Idea: a = 1, 2, 3, ...
        ## Complexity: Time O(log2(n)*log2(n)), Space O(1)
        import math
        a = 0
        while (a*a <= c):
            v = c-a*a
            k = int(math.sqrt(v))
            if k*k == v:
                return True
            a += 1
        return False
