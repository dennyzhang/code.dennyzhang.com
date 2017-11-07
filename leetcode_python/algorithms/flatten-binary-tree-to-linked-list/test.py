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
##     https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
##    ,-----------
##    | Given a binary tree, flatten it to a linked list in-place.
##    | 
##    | For example,
##    | Given
##    | 
##    |          1
##    |         / \
##    |        2   5
##    |       / \   \
##    |      3   4   6
##    | The flattened tree should look like:
##    |    1
##    |     \
##    |      2
##    |       \
##    |        3
##    |         \
##    |          4
##    |           \
##    |            5
##    |             \
##    |              6
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
