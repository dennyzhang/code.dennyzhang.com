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
##     https://leetcode.com/problems/binary-tree-paths/description/
##    ,-----------
##    | Given a binary tree, return all root-to-leaf paths.
##    | 
##    | For example, given the following binary tree:
##    | 
##    |    1
##    |  /   \
##    | 2     3
##    |  \
##    |   5
##    | All root-to-leaf paths are:
##    | 
##    | ["1->2->5", "1->3"]
##    | Credits:
##    | Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ## Idea: DFS recursive
        ## Complexity:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        res = []
        if root.left:
            for string in self.binaryTreePaths(root.left):
                res.append("%s->%s" % (str(root.val), string))

        if root.right:
            for string in self.binaryTreePaths(root.right):
                res.append("%s->%s" % (str(root.val), string))

        return res
