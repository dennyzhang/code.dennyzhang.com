# Leetcode: Remove Nth Node From End of List     :BLOG:Basic:


---

Remove Nth Node From End of List  

---

Given a linked list, remove the nth node from the end of list and return its head.  

For example,  

Given linked list: 1->2->3->4->5, and n = 2.  

After removing the second node from the end, the linked list becomes 1->2->3->5.  

Note:  
Given n will always be valid.  
Try to do this in one pass.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-nth-node-from-end-of-list)  

Credits To: [Leetcode.com](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)  

Leave me comments, if you know how to solve.  

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            ## Basic Idea:
            ##       1 -> 2  -> 3 -> 4 -> 5, n=2
            ##                  p   q   r
            ## Complexity: Time O(n), Space O(1)
            length = 0
            p = head
            while (p is not None):
                length += 1
                p = p.next
    
            if length < n:
                raise Exception("Link only have %d nodes. Can't delete %d th node" % (length, n))
    
            # remove the head
            if n == length:
                return head.next
    
            p = head
            # move the pointer
            for i in range(0, length - n - 1):
                p = p.next
    
            # remove the node
            q = p.next
            r = q.next
            p.next = r
            return head