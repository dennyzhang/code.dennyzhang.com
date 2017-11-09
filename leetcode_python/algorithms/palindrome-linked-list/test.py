#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/palindrome-linked-list/description/
##    ,-----------
##    | Given a singly linked list, determine if it is a palindrome.
##    | 
##    | Follow up:
##    | Could you do it in O(n) time and O(1) space?
##    `-----------
##
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## Idea: Can I destroy existing link?
        ##       1. Insert the last half into the head: 
        ##          From: a->b->c->b->a
        ##          To:   a->b->a->b->c
        ##       Then two pointers to check
        ## Complexity:
        if head is None or head.next is None:
            return True
        # find length
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        dummy = ListNode(None)
        dummy.next = head

        p = dummy
        for i in xrange((length+1)/2):
            p = p.next
        q = p
        p = dummy
        # move sublist to the head
        ## dummy -> a -> b
        ##   p      q    r
        for i in xrange(length/2):
            r = q.next
            q.next = r.next
            r.next = p.next
            p.next = r
        # move 2 pointers
        p = dummy
        for i in xrange(length/2):
            p = p.next
        q = p
        p = dummy
        for i in xrange(length/2):
            if p.next.val != q.next.val:
                return False
            p = p.next
            q = q.next
        return True
