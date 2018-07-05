
# Leetcode: Linked List Components     :BLOG:Basic:

---

Linked List Components  

---

Similar Problems:  

-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist)
-   Tag: [#linkedlist](https://code.dennyzhang.com/tag/linkedlist)

---

We are given head, the head node of a linked list containing unique integer values.  

We are also given the list G, a subset of the values in the linked list.  

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.  

Example 1:  

    Input: 
    head: 0->1->2->3
    G = [0, 1, 3]
    Output: 2
    Explanation: 
    0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:  

    Input: 
    head: 0->1->2->3->4
    G = [0, 3, 1, 4]
    Output: 2
    Explanation: 
    0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Note:  

-   If N is the length of the linked list given by head, 1 <= N <= 10000.
-   The value of each node in the linked list will be in the range [0, N - 1].
-   1 <= G.length <= 10000.
-   G is a subset of all values in the linked list.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/linked-list-components)  

Credits To: [leetcode.com](https://leetcode.com/problems/linked-list-components/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/linked-list-components
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution:
        def numComponents(self, head, G):
    	"""
    	:type head: ListNode
    	:type G: List[int]
    	:rtype: int
    	"""
    	## Basic Ideas: One pass for linked list
    	##              set
    	## Complexity: Time O(n), Space O(n)
    	nodes_set = set(G)
    	res = 0
    	node = head
    	new_start = True
    	while node:
    	    if node.val in nodes_set:
    		if new_start:
    		    res += 1
    		    new_start = False
    	    else:
    		new_start = True
    	    node = node.next
    	return res

