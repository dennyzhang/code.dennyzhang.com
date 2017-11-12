#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/subtree-of-another-tree/description/
##    ,-----------
##    | Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
##    | 
##    | Example 1:
##    | Given tree s:
##    | 
##    |      3
##    |     / \
##    |    4   5
##    |   / \
##    |  1   2
##    | Given tree t:
##    |    4 
##    |   / \
##    |  1   2
##    | Return true, because t has the same structure and node values with a subtree of s.
##    | Example 2:
##    | Given tree s:
##    | 
##    |      3
##    |     / \
##    |    4   5
##    |   / \
##    |  1   2
##    |     /
##    |    0
##    | Given tree t:
##    |    4
##    |   / \
##    |  1   2
##    | Return false.
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
