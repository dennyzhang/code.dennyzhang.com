#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #todobrain, #basic, #tree
## Description:
##     https://leetcode.com/problems/binary-tree-inorder-traversal/description/
##    ,-----------
##    | Given a binary tree, return the inorder traversal of its nodes' values.
##    | 
##    | For example:
##    | Given binary tree [1,null,2,3],
##    |    1
##    |     \
##    |      2
##    |     /
##    |    3
##    | return [1,3,2].
##    | 
##    | Note: Recursive solution is trivial, could you do it iteratively?
##    `-----------
##
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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack = []
        p = root
        # initialize the stack
        while p:
            stack.append(p)
            p = p.left

        # DFS
        while(len(stack) != 0):
            top_item = stack.pop()
            res.append(top_item.val)
            if top_item.right:
                p = top_item.right
                while p:
                    stack.append(p)
                    p = p.left
        return res

    def inorderTraversal_v1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.inorderTraversalRec(root, l)
        return l
    
    def inorderTraversalRec(self, root, list_value):
        if root is None:
            return

        if root.left is not None:
            self.inorderTraversalRec(root.left, list_value)
        
        list_value.append(root.val)

        if root.right is not None:
            self.inorderTraversalRec(root.right, list_value)
