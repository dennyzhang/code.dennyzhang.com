#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #todobrain
## Description:
##     https://leetcode.com/problems/arranging-coins/description/
##    ,-----------
##    | You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
##    | 
##    | Given n, find the total number of full staircase rows that can be formed.
##    | 
##    | n is a non-negative integer and fits within the range of a 32-bit signed integer.
##    | 
##    | Example 1:
##    | 
##    | n = 5
##    | 
##    | The coins can form the following rows:
##    | ¤
##    | ¤ ¤
##    | ¤ ¤
##    | 
##    | Because the 3rd row is incomplete, we return 2.
##    | Example 2:
##    | 
##    | n = 8
##    | 
##    | The coins can form the following rows:
##    | ¤
##    | ¤ ¤
##    | ¤ ¤ ¤
##    | ¤ ¤
##    | 
##    | Because the 4th row is incomplete, we return 3.
##    `-----------
##
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Idea: sqrt(2*n), then start with it
        import math
        k = (int)(math.sqrt(2*n))
        while k*(k+1) < 2*n:
            k = k + 1
        if k*(k+1) == 2*n:
            return k
        else:
            return k-1
