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
##     https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
##    ,-----------
##    | Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
##    | 
##    | Assume a BST is defined as follows:
##    | 
##    | The left subtree of a node contains only nodes with keys less than or equal to the node's key.
##    | The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
##    | Both the left and right subtrees must also be binary search trees.
##    | For example:
##    | Given BST [1,null,2,2],
##    |    1
##    |     \
##    |      2
##    |     /
##    |    2
##    | return [2].
##    | 
##    | Note: If a tree has more than one mode, you can return them in any order.
##    | 
##    | Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
##    `-----------
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
