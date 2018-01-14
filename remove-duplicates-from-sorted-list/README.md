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

    ## Basic Ideas: p points to the last processed node
    ## Complexity:
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
            if head is None:
                return None
            p = head
            q = head.next
            while q:
                if q.val == p.val:
                    q = q.next
                else:
                    # add q to the result list
                    r = q.next
                    p.next = q
                    p = p.next
                    q = r
            p.next = None
            return head