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
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Idea: start from sqrt(2*n)
        ## Complexity
        import math
        k = int(math.sqrt(2*n))
        sum_value = (k+1)*k/2
        while sum_value <= n:
            k += 1
            sum_value += k
        return k-1
