# Leetcode: Reverse Nodes in k-Group     :BLOG:Hard:


---

Identity number which appears exactly once.  

---

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.  

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.  

You may not alter the values in the nodes, only nodes itself may be changed.  

Only constant memory is allowed.  

    For example,
    Given this linked list: 1->2->3->4->5
    
    For k = 2, you should return: 2->1->4->3->5
    
    For k = 3, you should return: 3->2->1->4->5

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-nodes-in-k-group)  

Credits To: [Leetcode.com](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)  

Leave me comments, if you know how to solve.  

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reverseKGroup(self, head, k):
            """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
            """