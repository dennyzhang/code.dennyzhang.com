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
##     https://leetcode.com/problems/path-sum-ii/description/
##    ,-----------
##    | Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
##    | 
##    | For example:
##    | Given the below binary tree and sum = 22,
##    |               5
##    |              / \
##    |             4   8
##    |            /   / \
##    |           11  13  4
##    |          /  \    / \
##    |         7    2  5   1
##    | return
##    | [
##    |    [5,4,11,2],
##    |    [5,8,4,5]
##    | ]
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
