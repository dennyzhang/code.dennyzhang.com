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
##     https://leetcode.com/problems/symmetric-tree/description/
##    ,-----------
##    | Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
##    | 
##    | For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
##    | 
##    |     1
##    |    / \
##    |   2   2
##    |  / \ / \
##    | 3  4 4  3
##    | But the following [1,2,2,null,3,null,3] is not:
##    |     1
##    |    / \
##    |   2   2
##    |    \   \
##    |    3    3
##    | Note:
##    | Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ## Idea: BFS. pop 2 elements each time.
        ## Complexity
        if root is None:
            return True
        if (root.left is None) is not (root.right is None):
            return False
        if root.left is None:
            return True

        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while len(queue) != 0:
            element1 = queue[-1]
            del queue[-1]
            element2 = queue[-1]
            del queue[-1]
            if element1.val != element2.val:
                return False

            if (element1.left is None) is not (element2.right is None):
                return False

            if (element1.left is not None):
                queue.append(element1.left)
                queue.append(element2.right)

            if (element1.right is None) is not (element2.left is None):
                return False

            if (element1.right is not None):
                queue.append(element1.right)
                queue.append(element2.left)
        return True

    def isSymmetric_v1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self._isSymmetric(root.left, root.right)
        else:
            return True

    def _isSymmetric(self, node1, node2):
        if node1 is None or node2 is None:
            return (node1 is None) is (node2 is None)

        if node1.val != node2.val:
            return False
        else:
            return self._isSymmetric(node1.left, node2.right) and \
                    self._isSymmetric(node1.right, node2.left)
