#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/intersection-of-two-linked-lists/description/
##    ,-----------
##    | Write a program to find the node at which the intersection of two singly linked lists begins.
##    | 
##    | 
##    | For example, the following two linked lists:
##    | 
##    | A:          a1 → a2
##    |                    ↘
##    |                      c1 → c2 → c3
##    |                    ↗            
##    | B:     b1 → b2 → b3
##    | begin to intersect at node c1.
##    | 
##    | 
##    | Notes:
##    | 
##    | If the two linked lists have no intersection at all, return null.
##    | The linked lists must retain their original structure after the function returns.
##    | You may assume there are no cycles anywhere in the entire linked structure.
##    | Your code should preferably run in O(n) time and use only O(1) memory.
##    `-----------
##
## Tags:
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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## Idea: get the count of two links
        ##       Skip the longer link with a proper offset.
        ##       Then compare two links node by node
        ## Complexity: Time O(n), Space O(1)
        p = headA
        length1 = 0
        while (p is not None):
            length1 += 1
            p = p.next

        q = headB
        length2 = 0
        while (q is not None):
            length2 += 1
            q = q.next

        p = headA
        q = headB
        if length1 > length2:
            offset = length1 - length2
            while offset != 0:
                p = p.next
                offset -= 1
        else:
            if length1 < length2:
                offset = length2 - length1
                while offset != 0:
                    q = q.next
                    offset -= 1
        # check items
        while (p is not None) and (p != q):
            p = p.next
            q = q.next
        return p        
        