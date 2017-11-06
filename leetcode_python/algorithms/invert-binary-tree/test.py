#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/invert-binary-tree/description/
##    ,-----------
##    | Invert a binary tree.
##    | 
##    |      4
##    |    /   \
##    |   2     7
##    |  / \   / \
##    | 1   3 6   9
##    | to
##    |      4
##    |    /   \
##    |   7     2
##    |  / \   / \
##    | 9   6 3   1
##    | Trivia:
##    | This problem was inspired by this original tweet by Max Howell:
##    | Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-03 10:14:57>
##-------------------------------------------------------------------
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ## Idea: x^n = x^(n/2) * x^(n/2) * x^(n%2)
        ## Complexity: Time O(log(n)), Space O(1)
        ## Sample Data:
        ##   pow(5, 3) = 5*5*5
        ##   pow(5, -3) = ?
        ##   pow(-5, 3) = (-5)*(-5)*(-5)
        ##   pow(5.1, 3) = 5.1*5.1*5.1
        ##   x^n = x^(n/2) * x^(n/2) * x^(n%2)
        ##   pow(x, -n) = 1/pow(x, n)
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 1:
            return x
        if(n>=2):
            val = self.myPow(x, n/2)
            return val*val*self.myPow(x, n%2)
