#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
##    ,-----------
##    | Given a linked list, remove the nth node from the end of list and return its head.
##    | 
##    | For example,
##    | 
##    |    Given linked list: 1->2->3->4->5, and n = 2.
##    | 
##    |    After removing the second node from the end, the linked list becomes 1->2->3->5.
##    | Note:
##    | Given n will always be valid.
##    | Try to do this in one pass.
##    `-----------
##    
##    
## Tags:
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ## Basic Idea:
        ##       1 -> 2  -> 3 -> 4 -> 5, n=2
        ##                  p   q   r
        ## Complexity: Time O(n), Space O(1)
        length = 0
        p = head
        while (p is not None):
            length += 1
            p = p.next

        if length < n:
            raise Exception("Link only have %d nodes. Can't delete %d th node" % (length, n))

        # remove the head
        if n == length:
            return head.next

        p = head
        # move the pointer
        for i in range(0, length - n - 1):
            p = p.next

        # remove the node
        q = p.next
        r = q.next
        p.next = r
        return head
## File: test.py ends
