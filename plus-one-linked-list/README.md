# Leetcode: Plus One Linked List     :BLOG:Basic:


---

Plus One Linked List  

---

Similar Problems:  
-   [Reverse Linked List](https://brain.dennyzhang.com/reverse-linked-list)
-   [Review: Linked List Problems](https://brain.dennyzhang.com/review-linkedlist)
-   Tag: [#linkedlist](https://brain.dennyzhang.com/tag/linkedlist)

---

Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.  

You may assume the integer do not contain any leading zero, except the number 0 itself.  

The digits are stored such that the most significant digit is at the head of the list.  

Example:  

    Input:
    1->2->3
    
    Output:
    1->2->4

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/plus-one-linked-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/plus-one-linked-list/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/plus-one-linked-list
    ## Basic Ideas: Reverse the link. Add 1 with possible carry. Then reverse it back
    ##
    ## Complexity:
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution:
        def plusOne(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            newHead = self.reverseLinkedList(head)
    
            p, has_carry = newHead, True
            while has_carry:
                p.val += 1
                if p.val >= 10:
                    p.val = p.val % 10
                    has_carry = True
                else:
                    has_carry = False
                # add one more node, if required
                if has_carry and p.next is None:
                    p.next = ListNode(0)
                p = p.next
    
            return self.reverseLinkedList(newHead)
    
        def reverseLinkedList(self, head):
            if head is None: return None
            if head.next is None: return head
            dummyNode = ListNode(None)
            dummyNode.next = head
            p = head.next
            head.next = None
            while p:
                q = p.next
                p.next = dummyNode.next
                dummyNode.next = p
                p = q
            return dummyNode.next