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
##     https://leetcode.com/problems/maximum-width-of-binary-tree/description/
##    ,-----------
##    | Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
##    | 
##    | The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
##    | 
##    | Example 1:
##    | Input: 
##    | 
##    |            1
##    |          /   \
##    |         3     2
##    |        / \     \  
##    |       5   3     9 
##    | 
##    | Output: 4
##    | Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
##    | Example 2:
##    | Input: 
##    | 
##    |           1
##    |          /  
##    |         3    
##    |        / \       
##    |       5   3     
##    | 
##    | Output: 2
##    | Explanation: The maximum width existing in the third level with the length 2 (5,3).
##    | Example 3:
##    | Input: 
##    | 
##    |           1
##    |          / \
##    |         3   2 
##    |        /        
##    |       5      
##    | 
##    | Output: 2
##    | Explanation: The maximum width existing in the second level with the length 2 (3,2).
##    | Example 4:
##    | Input: 
##    | 
##    |           1
##    |          / \
##    |         3   2
##    |        /     \  
##    |       5       9 
##    |      /         \
##    |     6           7
##    | Output: 8
##    | Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
##    | 
##    | 
##    | Note: Answer will in the range of 32-bit signed integer.
##    `-----------
##
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-06 09:42:17>
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
