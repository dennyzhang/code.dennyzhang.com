# Leetcode: Delete Node in a Linked List     :BLOG:Hard:


---

Delete Node in a Linked List  

---

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.  

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/delete-node-in-a-linked-list)  

Credits To: [Leetcode.com](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)  

Leave me comments, if you know how to solve.  

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def deleteNode(self, node):
            """
            :type node: ListNode
            :rtype: void Do not return anything, modify node in-place instead.
            """
            ## Idea: update the value p.val with p.next.val, then remove p.next
            ## Complexity: Time O(n), Space O(1)
            ## Data Sample
            ##    1 -> 2 -> 3 -> 4 -> 5
            ##              node p 
            p = node.next # q will always exist
            node.val = p.val
            node.next = p.next