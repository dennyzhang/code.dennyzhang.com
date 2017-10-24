#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/roman-to-integer/description/
## Basic Idea:
## Complexity:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 20:02:09>
##-------------------------------------------------------------------
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## Basic Idea:
        ##   1 -> 3 -> 4 -> 5
        ##   p   q   r
        ##   always insert to the head
        if head is None or head.next is None:
            return head

        p = head
        q = p.next
        p.next = None

        while True:
            r = q.next
            q.next = p
            p = q
            q = r
            if q is None:
                break
        return p
## File: test.py ends
