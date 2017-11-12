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
##     https://leetcode.com/problems/trim-a-binary-search-tree/description/
##    ,-----------
##    | Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
##    | 
##    | Example 1:
##    | Input: 
##    |     1
##    |    / \
##    |   0   2
##    | 
##    |   L = 1
##    |   R = 2
##    | 
##    | Output: 
##    |     1
##    |       \
##    |        2
##    | Example 2:
##    | Input: 
##    |     3
##    |    / \
##    |   0   4
##    |    \
##    |     2
##    |    /
##    |   1
##    | 
##    |   L = 1
##    |   R = 3
##    | 
##    | Output: 
##    |       3
##    |      / 
##    |    2   
##    |   /
##    |  1
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Idea: sqrt(num)
        ## Complexity:
        ## Sample Data:
        ##    1 2 7
        if num <= 1:
            return False
        import math
        sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sum += i
                if i != num/i:
                    sum += num/i
        return sum == num
