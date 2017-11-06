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
##     https://leetcode.com/problems/binary-tree-postorder-traversal/description/
##    ,-----------
##    | Given a binary tree, return the postorder traversal of its nodes' values.
##    | 
##    | For example:
##    | Given binary tree {1,#,2,3},
##    |    1
##    |     \
##    |      2
##    |     /
##    |    3
##    | return [3,2,1].
##    | 
##    | Note: Recursive solution is trivial, could you do it iteratively?
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        p = root
        # element: pointer, whether_visited_right
        while p:
            stack.append((p, False))
            p = p.left

        while len(stack) != 0:
            (top_element, whether_visited_right) = stack.pop()
            if whether_visited_right is False:
                if top_element.right:
                    stack.append((top_element, True))
                    p = top_element.right
                    while p:
                        stack.append((p, False))
                        p = p.left
                else:
                    res.append(top_element.val)
            else:
                res.append(top_element.val)

        return res

    def postorderTraversal_v1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorderTraversalRec(root, res)
        return res
        
    def postorderTraversalRec(self, root, list_value):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return
        if root.left:
            self.postorderTraversalRec(root.left, list_value)
        if root.right:
            self.postorderTraversalRec(root.right, list_value)
        list_value.append(root.val)
