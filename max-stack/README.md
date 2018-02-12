# Leetcode: Max Stack     :BLOG:Medium:


---

Max Stack  

---

Similar Problems:  
-   [Min Stack](https://brain.dennyzhang.com/min-stack)
-   Tag: [#designquestion](https://brain.dennyzhang.com/tag/designquestion)

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

    ## Blog link: https://brain.dennyzhang.com/max-stack