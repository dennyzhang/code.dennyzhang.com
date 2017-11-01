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
##     https://leetcode.com/problems/reverse-linked-list-ii/description/
##    ,-----------
##    | Reverse a linked list from position m to n. Do it in-place and in one-pass.
##    | 
##    | For example:
##    | Given 1->2->3->4->5->NULL, m = 2 and n = 4,
##    | 
##    | return 1->4->3->2->5->NULL.
##    | 
##    | Note:
##    | Given m, n satisfy the following condition:
##    | 1 ≤ m ≤ n ≤ length of list.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:14>
##-------------------------------------------------------------------
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        ## Basic Idea:
        ##   1->2->3->4->5->NULL, m = 2 and n = 4,
        ##      2->3->4
        ##   p  q     r  s
## File: test.py ends
