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
##     https://leetcode.com/problems/implement-stack-using-queues/description/
##    ,-----------
##    | Implement the following operations of a stack using queues.
##    | 
##    | push(x) -- Push element x onto stack.
##    | pop() -- Removes the element on top of the stack.
##    | top() -- Get the top element.
##    | empty() -- Return whether the stack is empty.
##    | Notes:
##    | You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
##    | Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
##    | You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-26 18:12:36>
##-------------------------------------------------------------------
class MyStack(object):
    ## Idea: Use 1 queue
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        length = len(self.queue)
        self.queue.append(x)
        for i in range(0, length):
            item = self.queue[0]
            del self.queue[0]
            self.queue.append(item)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        item = self.queue[0]
        del self.queue[0]
        return item
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class MyStack1(object):
    ## Idea: Use 2 queue
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        ## Complexity: Time O(n), Space O(n)
        # move queue1 to queue2
        return self.move(True)
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.move(False)

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0

    def move(self, whether_delete):
        """
        Move items from queue1 to queue2
        :whether_pop: bool
        :rtype: int
        """
        ret = None
        while len(self.queue1) != 0:
            item = self.queue1[0]
            if len(self.queue1) == 1:
                ret = item
                if whether_delete is False:
                    self.queue2.append(item)
            else:
                self.queue2.append(item)
            del self.queue1[0]

        # move back
        while len(self.queue2) != 0:
            item = self.queue2[0]
            del self.queue2[0]
            self.queue1.append(item)
        return ret

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
