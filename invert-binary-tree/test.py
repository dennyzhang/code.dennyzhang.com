#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ## Idea: BFS
        ## Complexity:
        if root is None:
            return root
        queue = []
        queue.append(root)
        while len(queue) != 0:
            element = queue.pop()
            p = element.left
            element.left = element.right
            element.right = p
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
        return root

    def invertTree_v1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if (root.left is None) and (root.right is None):
            return root

        if (root.left is None) and root.right:
            root.left = self.invertTree(root.right)
            root.right = None
            return root

        if (root.right is None) and root.left:
            root.right = self.invertTree(root.left)
            root.left = None
            return root

        p = self.invertTree(root.left)
        q = self.invertTree(root.right)
        root.left = q
        root.right = p
        return root
