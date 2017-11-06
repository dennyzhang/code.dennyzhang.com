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
##     https://leetcode.com/problems/validate-binary-search-tree/description/
##    ,-----------
##    | Given a binary tree, determine if it is a valid binary search tree (BST).
##    | 
##    | Assume a BST is defined as follows:
##    | 
##    | The left subtree of a node contains only nodes with keys less than the node's key.
##    | The right subtree of a node contains only nodes with keys greater than the node's key.
##    | Both the left and right subtrees must also be binary search trees.
##    | Example 1:
##    |     2
##    |    / \
##    |   1   3
##    | Binary tree [2,1,3], return true.
##    | Example 2:
##    |     1
##    |    / \
##    |   2   3
##    | Binary tree [1,2,3], return false.
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
