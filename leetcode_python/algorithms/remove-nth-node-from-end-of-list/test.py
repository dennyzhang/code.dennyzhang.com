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
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MinStack(object):

    ## Idea: List with elements of (value, min_value)
    ## 
    ## -2 0 -3  4
    ## linked list:
    ##     (-2, -2), (0, -2), (-3, -3), (4, -3)
    ##
    ## length: element count
    ##
    ##
    ## Complexity:  Time: O(1), Space: O(n)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.length = 0
        self.min_value = None
        self.values = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.length == 0:
            element = (x, x)
            self.min_value = x
        else:
            if x > self.min_value:
                element = (x, self.min_value)
            else:
                self.min_value = x
                element = (x, x)
        self.values.append(element)
        self.length += 1

    def pop(self):
        """
        :rtype: void
        """
        if self.length == 0:
            return

        if self.length == 1:
            self.min_value = None
        else:
            (x, previous_min_value) = self.values[-2]
            self.min_value = previous_min_value

        self.values.pop()
        self.length -= 1

    def top(self):
        """
        :rtype: int
        """
        if len(self.values) == 0:
            return None
        else:
            (x, _min_value) = self.values[-1]
            return x

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
