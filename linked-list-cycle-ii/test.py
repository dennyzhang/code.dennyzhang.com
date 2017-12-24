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
##     https://leetcode.com/problems/roman-to-integer/description/
##    ,-----------
##    | Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
##    | 
##    | Note: Do not modify the linked list.
##    | 
##    | Follow up:
##    | Can you solve it without using extra space?
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:14>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## Ideas: Two pointers: one move one step, the other move 2 steps each time.
        ##                      If the two pointers meet, we have the circle. Otherwise we don't.
        ##                      m == n
        ## Complexity: Time O(n), Space O(1)
        if head is None:
            return None
        p = head
        q = head
        while True:
            p = p.next
            if q.next is None:
                q = None
                break
            q = q.next.next
            if (q is None) or (p == q):
                break

        if q is None:
            return None
        else:
            # move one pointer back to head
            p = head
            while(p!=q):
                p = p.next
                q = q.next
            return p
