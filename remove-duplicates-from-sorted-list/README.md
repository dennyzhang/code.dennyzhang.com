# Leetcode: Remove Duplicates from Sorted List     :BLOG:Basic:


---

Delete duplicate nodes from a sorted linked list  

---

Given a sorted linked list, delete all duplicates such that each element appear only once.  

For example,  
Given 1->1->2, return 1->2.  
Given 1->1->2->3->3, return 1->2->3.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-duplicates-from-sorted-list)  

Credits To: [Leetcode.com](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: 
    ## Complexity: Time O(n), Space O(1)
    ##  1 -> 1 -> 1-> 2 -> 3 -> 3
    ##  p    q    r
    
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if (head is None) or (head.next is None):
                return head
            p = head
            q = p.next
            while (q is not None):
                while (q is not None) and (p.val == q.val):
                    q = q.next
                    p.next = q
                if q is not None:
                    r = q.next
                    p = q
                    q = r
            return head