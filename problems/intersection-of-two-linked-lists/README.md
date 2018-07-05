
# Leetcode: Intersection of Two Linked Lists     :BLOG:Basic:

---

Intersection of Two Linked Lists  

---

Write a program to find the node at which the intersection of two singly linked lists begins.  

For example, the following two linked lists:  

    A:          a1 -> a2
                        \
                         c1 -> c2 -> c3
                       /            
    B:     b1 -> b2 -> b3
    begin to intersect at node c1.

Notes:  

-   If the two linked lists have no intersection at all, return null.
-   The linked lists must retain their original structure after the function returns.
-   You may assume there are no cycles anywhere in the entire linked structure.
-   Your code should preferably run in O(n) time and use only O(1) memory.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/intersection-of-two-linked-lists)  

Credits To: [leetcode.com](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/intersection-of-two-linked-lists
    ## Basic Ideas: get the count of two links
    ##       Skip the longer link with a proper offset.
    ##       Then compare two links node by node
    ## Complexity: Time O(n), Space O(1)
    
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

