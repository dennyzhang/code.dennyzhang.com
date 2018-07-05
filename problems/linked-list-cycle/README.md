
# Leetcode: Linked List Cycle     :BLOG:Basic:

---

Linked List Cycle  

---

Similar Problems:  

-   [Review: TwoPointers Problems](https://code.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Given a linked list, determine if it has a cycle in it.  

Follow up:  
Can you solve it without using extra space?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/linked-list-cycle)  

Credits To: [leetcode.com](https://leetcode.com/problems/linked-list-cycle/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/linked-list-cycle
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def hasCycle(self, head):
    	"""
    	:type head: ListNode
    	:rtype: bool
    	"""
    	## Idea: 2 pointers. Each time, p1 move 1 step, p2 move 2 step. 
    	##         If it has a cycle(not only it's a circle), p1 and p2 will meet. 
    	##         Otherwise p1 and p2 won't.
    	## Complexity: Time O(n), Space O(1)
    	##
    	##     n1    ->   n2    -> n3
    	##     p1
    	##                p2
    	if head is None or head.next is None:
    	    return False
    	p1 = head
    	p2 = head.next
    	while (p1 is not None) and (p2 is not None) and (p2 != p1):
    	    p1 = p1.next
    	    if (p2.next is None) or (p2.next is None):
    		p2 = None
    	    else:
    		p2 = p2.next.next
    
    	return  (p1 is not None) and (p2 is not None) and (p2 == p1)

