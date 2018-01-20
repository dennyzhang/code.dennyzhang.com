# Leetcode: Implement Stack using Queues     :BLOG:Medium:


---

Implement Stack using Queues  

---

Implement the following operations of a stack using queues.  

-   push(x) &#x2013; Push element x onto stack.
-   pop() &#x2013; Removes the element on top of the stack.
-   top() &#x2013; Get the top element.
-   empty() &#x2013; Return whether the stack is empty.

Notes:  
-   You must use only standard operations of a queue &#x2013; which means only push to back, peek/pop from front, size, and is empty operations are valid.
-   Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
-   You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

Blog link: <http://brain.dennyzhang.com/implement-stack-using-queues>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/implement-stack-using-queues)  

Credits To: [leetcode.com](https://leetcode.com/problems/implement-stack-using-queues/description)  

Leave me comments, if you know how to solve.  

    class MyQueue(object):
    
        ## Idea: Use 2 stack. When pop, move to stack1, then stack2
        ## Complexity: Time O(n), Space O(n)
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.stack1 = []
            self.stack2 = []
    
    
        def push(self, x):
            """
            Push element x to the back of queue.
            :type x: int
            :rtype: void
            """
            self.stack1.append(x)
    
        def pop(self):
            """
            Removes the element from in front of queue and returns that element.
            :rtype: int
            """
            ## Complexity: Time O(n), Space: O(n)
            # move elements from stack1 to stack2
            ret = None
            while len(self.stack1) != 0:
                item = self.stack1[-1]
                del self.stack1[-1]
                self.stack2.append(item)
            ret = self.stack2[-1]
            del self.stack2[-1]
    
            # push back to stack2
            while len(self.stack2) != 0:
                item = self.stack2[-1]
                del self.stack2[-1]
                self.stack1.append(item)
            return ret
    
        def peek(self):
            """
            Get the front element.
            :rtype: int
            """
            ## Complexity: Time O(n), Space: O(n)
            # move elements from stack1 to stack2
            ret = None
            while len(self.stack1) != 0:
                item = self.stack1[-1]
                del self.stack1[-1]
                self.stack2.append(item)
            ret = self.stack2[-1]
    
            # push back to stack2
            while len(self.stack2) != 0:
                item = self.stack2[-1]
                del self.stack2[-1]
                self.stack1.append(item)
            return ret
    
        def empty(self):
            """
            Returns whether the queue is empty.
            :rtype: bool
            """
            return len(self.stack1) == 0
    
    
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()