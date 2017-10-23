#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/same-tree/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:12>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None) and (q is None):
            return True
        else:
            if (p is None) or (q is None):
                return False
            else:
                if p.val != q.val:
                    return False
                else:
                    # recursive way
                    if self.isSameTree(p.left, q.left) is False:
                        return False
                    if self.isSameTree(p.right, q.right) is False:
                        return False
                    return True
