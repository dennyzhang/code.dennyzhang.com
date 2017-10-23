#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/rotate-list/description/
## Basic Idea:
##      1->2->3->4->5->NULL
##      1->2->3->    4->5->NULL
##    head    p      q  r
##
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 17:51:11>
##-------------------------------------------------------------------
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        p = head
        length = 1
        while p.next is not None:
            length += 1
            p = p.next

        k = k % length
        if k == 0:
            return head

        p = head
        for i in range(0, length-k-1):
            p = p.next

        q = p.next
        r = q
        while r.next is not None:
            r = r.next
        r.next = head
        p.next = None
        head = q
        return head
## File: test.py ends
