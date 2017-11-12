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
##     https://leetcode.com/problems/house-robber-iii/description/
##    ,-----------
##    | The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
##    | 
##    | Determine the maximum amount of money the thief can rob tonight without alerting the police.
##    | 
##    | Example 1:
##    |      3
##    |     / \
##    |    2   3
##    |     \   \ 
##    |      3   1
##    | Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
##    | Example 2:
##    |      3
##    |     / \
##    |    4   5
##    |   / \   \ 
##    |  1   3   1
##    | Maximum amount of money the thief can rob = 4 + 5 = 9.
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
