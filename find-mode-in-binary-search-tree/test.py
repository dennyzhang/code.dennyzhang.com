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
##     https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
##    ,-----------
##    | Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
##    | 
##    | Assume a BST is defined as follows:
##    | 
##    | The left subtree of a node contains only nodes with keys less than or equal to the node's key.
##    | The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
##    | Both the left and right subtrees must also be binary search trees.
##    | For example:
##    | Given BST [1,null,2,2],
##    |    1
##    |     \
##    |      2
##    |     /
##    |    2
##    | return [2].
##    | 
##    | Note: If a tree has more than one mode, you can return them in any order.
##    | 
##    | Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------c
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## Basic Idea: In-order traversal
        ## Complexity:
        
        res = []
        # in-order trasveral
        stack = []
        p = root
        while p:
            stack.append(p)
            p = p.left

        max_count = 0
        previous_val = None
        item_count = 0
        while len(stack) != 0:
            # print("item_count: %d, previous_val: %d, res: %s" % (item_count, previous_val if previous_val else -1, res))
            top_item = stack.pop()
            if previous_val is None:
                item_count = 1
                max_count = 1
                res.append(top_item.val)
            else:
                if top_item.val == previous_val:
                    item_count += 1
                else:
                    # reset the counter
                    item_count = 1
                if item_count == max_count:
                    res.append(top_item.val)
                else:
                    if item_count > max_count:
                        max_count = item_count
                        res = []
                        res.append(top_item.val)
            previous_val = top_item.val
            if top_item.right:
                p = top_item.right
                while p:
                    stack.append(p)
                    p = p.left
        return res
