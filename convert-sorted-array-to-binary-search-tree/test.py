#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
##
##    ,-----------
##    | Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
##    | 
##    | For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
##    | 
##    | 
##    | Example:
##    | 
##    | Given the sorted array: [-10,-3,0,5,9],
##    | 
##    | One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
##    | 
##    |       0
##    |      / \
##    |    -3   9
##    |    /   /
##    |  -10  5
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2018-01-08 11:07:32>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        ## Basic Idea: Find the middle node
        ## Complexity: Time O(n), Space O(1)
        ## Assumptions:
        ## Sample Data
        length = len(nums)
        if length == 0:
            return None
        mid_index = length/2
        head = TreeNode(nums[mid_index])
        head.left = self.sortedArrayToBST(nums[0:mid_index])
        head.right = self.sortedArrayToBST(nums[mid_index+1:])
        return head
