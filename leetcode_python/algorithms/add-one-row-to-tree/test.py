#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/add-one-row-to-tree/description/
##    ,-----------
##    | Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
##    | 
##    | The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.
##    | 
##    | Example 1:
##    | Input: 
##    | A binary tree as following:
##    |        4
##    |      /   \
##    |     2     6
##    |    / \   / 
##    |   3   1 5   
##    | 
##    | v = 1
##    | 
##    | d = 2
##    | 
##    | Output: 
##    |        4
##    |       / \
##    |      1   1
##    |     /     \
##    |    2       6
##    |   / \     / 
##    |  3   1   5   
##    | 
##    | Example 2:
##    | Input: 
##    | A binary tree as following:
##    |       4
##    |      /   
##    |     2    
##    |    / \   
##    |   3   1    
##    | 
##    | v = 1
##    | 
##    | d = 3
##    | 
##    | Output: 
##    |       4
##    |      /   
##    |     2
##    |    / \    
##    |   1   1
##    |  /     \  
##    | 3       1
##    | Note:
##    | The given d is in range [1, maximum depth of the given tree + 1].
##    | The given binary tree has at least one tree node.
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
