# Leetcode: Sort List     :BLOG:Basic:


---

Sort linked list  

---

Sort a linked list in O(n log n) time using constant space complexity.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sort-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/sort-list/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/sort-list
    ## Basic Ideas: Merge sort. Recursive
    ##       1. Divide the list into two half
    ##       2. Merge sort these two
    ##       3. Combine two sorted list
    ##          5  -> 6 -> 2 -> 7 -> 4
    ## Complexity: Time O(n*log(n)), Space O(1)
    
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def sortList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if head is None or head.next is None:
                return head
            length = 0
            prev, slow, fast = None, head, head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
    
            prev.next = None
            head1 = self.sortList(head)
            head2 = self.sortList(slow)
            return self.mysortList(head1, head2)
    
        def mysortList(self, head1, head2):
            # merge two sorted list
            dummyNode = ListNode(None)
            p, p1, p2 = dummyNode, head1, head2
            while p1 and p2:
                if p1.val <= p2.val:
                    # append p1 to the new list
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
    
            if p1 is None:
                p1 = p2
            p.next = p1
            return dummyNode.next