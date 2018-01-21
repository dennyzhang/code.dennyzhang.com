# Leetcode: Reverse Nodes in k-Group     :BLOG:Hard:


---

Reverse Nodes in k-Group  

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

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/reverse-nodes-in-k-group
    ## Basic Ideas: Two pointer(p1, p2) with distance of k
    ##              Since head node might be changed, add a dummyNode
    ##              How to process:
    ##                 If p2 is None, stop changing
    ##                 Otherwise reverse list from p1 to p2
    ##              Move to next:
    ##                 p2 move to right with k distance
    ##                 If p2 is None, stop changing
    ## Complexity: Time O(n), Space O(1)
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
            if k <= 1:
                return head
            dummyNode = ListNode(None)
            dummyNode.next = head
            p1 = dummyNode
    
            while True:
                p2 = p1
                for i in xrange(k):
                    if p2 is None:
                        break
                    p2 = p2.next
    
                if p2 is None:
                    break
    
                # save the pointer of next p1
                q, s = p1.next, p2.next
                # reverse list from p1 to p2
                p = p1.next.next
                p1.next.next = s
                while p != s:
                    r = p.next
                    p.next = p1.next
                    p1.next = p
                    # move to next
                    p = r
                p1 = q
            return dummyNode.next