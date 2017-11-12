#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
## ,-----------
## | Given a sorted linked list, delete all duplicates such that each element appear only once.
## | 
## | For example,
## | Given 1->1->2, return 1->2.
## | Given 1->1->2->3->3, return 1->2->3.
## `-----------
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## Idea: 
        ## Complexity: Time O(n), Space O(1)
        ##  1 -> 1 -> 1-> 2 -> 3 -> 3
        ##  p    q    r
        if (head is None) or (head.next is None):
            return head
        p = head
        q = p.next
        while (q is not None):
            while (q is not None) and (p.val == q.val):
                q = q.next
                p.next = q
            if q is not None:
                r = q.next
                p = q
                q = r
        return head
