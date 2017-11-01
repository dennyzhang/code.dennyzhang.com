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
##     https://leetcode.com/problems/min-stack/description/
##    ,-----------
##    | Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
##    | 
##    | push(x) -- Push element x onto stack.
##    | pop() -- Removes the element on top of the stack.
##    | top() -- Get the top element.
##    | getMin() -- Retrieve the minimum element in the stack.
##    | Example:
##    | MinStack minStack = new MinStack();
##    | minStack.push(-2);
##    | minStack.push(0);
##    | minStack.push(-3);
##    | minStack.getMin();   --> Returns -3.
##    | minStack.pop();
##    | minStack.top();      --> Returns 0.
##    | minStack.getMin();   --> Returns -2.
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 23:24:46>
##-------------------------------------------------------------------
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_val = None
        self.values = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.values.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.values.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.values) == 0:
            return None
        else:
            return self.values[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.values) == 0:
            return None
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
## File: test.py ends
