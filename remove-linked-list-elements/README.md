# Leetcode: Remove Linked List Elements     :BLOG:Basic:


---

Remove Linked List Elements  

---

Remove all elements from a linked list of integers that have value val.  

Example  
Given: 1 &#x2013;> 2 &#x2013;> 6 &#x2013;> 3 &#x2013;> 4 &#x2013;> 5 &#x2013;> 6, val = 6  
Return: 1 &#x2013;> 2 &#x2013;> 3 &#x2013;> 4 &#x2013;> 5  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-linked-list-elements)  

Credits To: [leetcode.com](https://leetcode.com/problems/remove-linked-list-elements/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/remove-linked-list-elements
    ## Basic Ideas: The head might be removed, thus we need a dummy node
    ## Complexity: Time O(n), Space O(1)
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeElements(self, head, val):
            """
            :type head: ListNode
            :type val: int
            :rtype: ListNode
            """
            dummyNode = ListNode(None)
            dummyNode.next = head
            p = dummyNode
            while p.next:
                if p.next.val == val:
                    p.next = p.next.next
                else:
                    p = p.next
            return dummyNode.next