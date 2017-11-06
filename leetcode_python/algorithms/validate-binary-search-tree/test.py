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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ## Idea: DFS recursive
        ## Complexity: Time O(n), Space O(log(n))
        list_value = self.getBST(root)
        for i in range(0, len(list_value)-1):
            if list_value[i+1] <= list_value[i]:
                return False
        return True

    def getBST(self, root):
        if root is None:
            return []

        res = []
        if root.left:
            res += self.getBST(root.left)

        res.append(root.val)

        if root.right:
            res += self.getBST(root.right)
        return res
