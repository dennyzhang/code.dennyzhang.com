# Leetcode: Odd Even Linked List     :BLOG:Basic:


---

Odd Even Linked List  

---

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.  

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.  

    Example:
    Given 1->2->3->4->5->NULL,
    return 1->3->5->2->4->NULL.

Note:  
-   The relative order inside both the even and odd groups should remain as it was in the input.
-   The first node is considered odd, the second node even and so on &#x2026;

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/odd-even-linked-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/odd-even-linked-list/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/odd-even-linked-list
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def oddEvenList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            ## Idea: 2pointer: odd_tail, even_tail
            ##       move the next element of even_tail to odd_tail
            ##       move next for both tails
            ## Complexity
            ## Sample Data:
            ##       1    ->    2  ->    3   ->   4   ->   5   ->NULL
            ##    odd_tail even_tail
            ##
            if head is None or head.next is None:
                return head
            odd_tail = head
            even_tail = head.next
            while even_tail and even_tail.next:
                p = even_tail.next
                even_tail.next = p.next
                p.next = odd_tail.next
                odd_tail.next = p
                # move next
                even_tail = even_tail.next
                odd_tail = odd_tail.next
            return head