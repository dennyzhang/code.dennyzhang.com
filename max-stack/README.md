# Leetcode: Max Stack     :BLOG:Medium:


---

Max Stack  

---

Similar Problems:  
-   [Min Stack](https://code.dennyzhang.com/min-stack)
-   [Insert Delete GetRandom O(1) – Duplicates allowed](https://code.dennyzhang.com/insert-delete-getrandom-o1-duplicates-allowed)
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign), Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Design a max stack that supports push, pop, top, peekMax and popMax.  

1.  push(x) &#x2013; Push element x onto stack.
2.  pop() &#x2013; Remove the element on top of the stack and return it.
3.  top() &#x2013; Get the element on the top.
4.  peekMax() &#x2013; Retrieve the maximum element in the stack.
5.  popMax() &#x2013; Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:  

    MaxStack stack = new MaxStack();
    stack.push(5); 
    stack.push(1);
    stack.push(5);
    stack.top(); -> 5
    stack.popMax(); -> 5
    stack.top(); -> 1
    stack.peekMax(); -> 5
    stack.pop(); -> 1
    stack.top(); -> 5

Note:  
1.  -1e7 <= x <= 1e7
2.  Number of operations won't exceed 10000.
3.  The last four operations won't be called when stack is empty.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/max-stack)  

Credits To: [leetcode.com](https://leetcode.com/problems/max-stack/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/max-stack
    ## Basic Ideas: 2 stacks
    ##
    ## Complexity: Time: topMax O(n), others O(1)
    ##             Space: O(1)
    class MaxStack:
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.stack = []
            self.maxStack = []
    
        def pushHelper(self, x):
            self.stack.append(x)
            max_v = x
            if len(self.maxStack) != 0 and self.maxStack[-1] > max_v:
                max_v = self.maxStack[-1]
            self.maxStack.append(max_v)
    
        def push(self, x):
            """
            :type x: int
            :rtype: void
            """
            self.pushHelper(x)
    
    
        def pop(self):
            """
            :rtype: int
            """
            self.maxStack.pop()
            return self.stack.pop()
    
    
        def top(self):
            """
            :rtype: int
            """
            return self.stack[-1]
    
    
        def peekMax(self):
            """
            :rtype: int
            """
            return self.maxStack[-1]
    
    
        def popMax(self):
            """
            :rtype: int
            """
            max_v = self.maxStack[-1]
            tmpStack = []
            while self.stack[-1] != max_v:
                tmpStack.append(self.stack.pop())
                self.maxStack.pop()
            self.stack.pop()
            self.maxStack.pop()
            while len(tmpStack) != 0:
                self.pushHelper(tmpStack.pop())
            return max_v
    
    # Your MaxStack object will be instantiated and called as such:
    # obj = MaxStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.peekMax()
    # param_5 = obj.popMax()