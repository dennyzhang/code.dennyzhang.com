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
##     https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
##    ,-----------
##    | Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
##    | 
##    | An example is the root-to-leaf path 1->2->3 which represents the number 123.
##    | 
##    | Find the total sum of all root-to-leaf numbers.
##    | 
##    | For example,
##    | 
##    |     1
##    |    / \
##    |   2   3
##    | The root-to-leaf path 1->2 represents the number 12.
##    | The root-to-leaf path 1->3 represents the number 13.
##    | 
##    | Return the sum = 12 + 13 = 25.
##    `-----------
##
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
