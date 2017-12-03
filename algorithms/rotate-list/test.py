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
##     https://leetcode.com/problems/rotate-list/description/
##    ,-----------
##    | Given a list, rotate the list to the right by k places, where k is non-negative.
##    | 
##    | 
##    | Example:
##    | 
##    | Given 1->2->3->4->5->NULL and k = 2,
##    | 
##    | return 4->5->1->2->3->NULL.
##    `-----------
##
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ## Basic Idea: 
        ##       Get length of the list
        ##       pointer q: where to rotate
        ##
        ## Complexity: Time O(n), Space O(1)
        ## Assumptions:
        ## Sample Data:
        ##        1->2->3->4->5->NULL
        ##              q   last_node
        # empty list
        if head is None or k == 0:
            return head
        # get length
        p = head
        length = 0
        last_node = None
        while p:
            if p.next is None:
                last_node = p
            length += 1
            p = p.next
            
        if k >= length:
            k = k % length

        # Highlight: why we need this special case?
        if k == 0:
            return head

        q = head

        # Highlight: How many steps you shall move?
        for i in xrange(length-k-1):
            q = q.next

        res = q.next
        q.next = None
        last_node.next = head
        return res
        