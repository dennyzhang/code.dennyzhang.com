#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/delete-node-in-a-linked-list/description/
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 08:36:47>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ## Idea: update the value p.val with p.next.val, then remove p.next
        ## Complexity: Time O(n), Space O(1)
        ## Data Sample
        ##    1 -> 2 -> 3 -> 4 -> 5
        ##              node p 
        p = node.next # q will always exist
        node.val = p.val
        node.next = p.next
