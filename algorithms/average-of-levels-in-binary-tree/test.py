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
##     https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
##    ,-----------
##    | Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
##    | 
##    | Example 1:
##    | Input:
##    |     3
##    |    / \
##    |   9  20
##    |     /  \
##    |    15   7
##    | Output: [3, 14.5, 11]
##    | Explanation:
##    | The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
##    | Note:
##    | The range of node's value is in the range of 32-bit signed integer.
##    `-----------
##
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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ## Idea: BFS
        ## Complexity: Time O(n), Space O(k)
        if root is None:
            return []
        res = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            length = len(queue)
            average_level = 0
            for i in xrange(length):
                element = queue[0]
                del queue[0]
                average_level += element.val
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.append(float(average_level)/length)
        return res
