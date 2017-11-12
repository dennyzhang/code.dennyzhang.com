#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/merge-two-sorted-lists/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:59:17>
##-------------------------------------------------------------------
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## Basic Idea:
        ##    l1: 1 -> 3 -> 5
        ##        p   r
        ##    l2: 2 -> 3 -> 6 -> 7
        ##        q   s
        ## Complexity:
        ## recursive
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = l1        
            p = l1
            q = l2
        else:
            head = l2
            p = l2
            q = l1

        while (p.next is not None) and (q is not None):
            r = p.next
            s = q.next
            if q.val <= r.val:
                p.next = q
                q.next = r
                p = q
                q = s
            else:
                p = r

        if p.next is None:
            p.next = q

        return head
## File: test.py ends
