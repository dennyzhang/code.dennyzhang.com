# Leetcode: Reverse Linked List     :BLOG:Basic:


---

Reverse Linked List  

---

Reverse a singly linked list.  

click to show more hints.  

Hint:  
A linked list can be reversed either iteratively or recursively. Could you implement both?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-linked-list)  

Credits To: [Leetcode.com](https://leetcode.com/problems/reverse-linked-list/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            ## Basic Idea:
            ##   1 -> 3 -> 4 -> 5
            ##   p   q   r
            ##   always insert to the head
            if head is None or head.next is None:
                return head
    
            p = head
            q = p.next
            p.next = None
    
            while True:
                r = q.next
                q.next = p
                p = q
                q = r
                if q is None:
                    break
            return p