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
##     https://leetcode.com/problems/remove-linked-list-elements/description/
##    ,-----------
##    | Remove all elements from a linked list of integers that have value val.
##    | 
##    | Example
##    | Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
##    | Return: 1 --> 2 --> 3 --> 4 --> 5
##    | 
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ## Idea:
        ## Complexity:
        ## Sample Data:
        ##  1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
        ##        p     q     r
        # When head is None, or keep removing the head
        while (head is not None) and (head.val == val):
            head = head.next
        if head is None:
            return head
        p = head
        q = p.next
        while q is not None:
            if q.val == val:
                # remove the node
                r = q.next
                p.next = r
                q = r
            else:
                p = q
                q = q.next
        return head
