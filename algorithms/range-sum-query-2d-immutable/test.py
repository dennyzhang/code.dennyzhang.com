#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #amusing
## Description:
##     https://leetcode.com/problems/range-sum-query-2d-immutable/description/
##    ,-----------
##    | Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
##    | 
##    | Range Sum Query 2D
##    | The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
##    | 
##    | Example:
##    | Given matrix = [
##    |   [3, 0, 1, 4, 2],
##    |   [5, 6, 3, 2, 1],
##    |   [1, 2, 0, 1, 5],
##    |   [4, 1, 0, 1, 7],
##    |   [1, 0, 3, 0, 5]
##    | ]
##    | 
##    | sumRegion(2, 1, 4, 3) -> 8
##    | sumRegion(1, 1, 2, 2) -> 11
##    | sumRegion(1, 2, 2, 4) -> 12
##    | Note:
##    | You may assume that the matrix does not change.
##    | There are many calls to sumRegion function.
##    | You may assume that row1 ≤ row2 and col1 ≤ col2.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-29 09:24:32>
##-------------------------------------------------------------------
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Basic Idea:
        ## Complexity:

if __name__ == '__main__':
    s = Solution()
    # print s.romanToInt("MCMXCVI")
