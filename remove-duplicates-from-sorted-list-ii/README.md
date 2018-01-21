# Leetcode: Remove Duplicates from Sorted List II     :BLOG:Hard:


---

Remove Duplicates from Sorted List II  

---

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.  

For example,  

Given 1->2->3->3->4->4->5, return 1->2->5.  

Given 1->1->1->2->3, return 2->3.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-duplicates-from-sorted-list-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/remove-duplicates-from-sorted-list-ii
    ## Basic Ideas:
    ##    p points to the last processed node
    ##    Whether to add one node
    ##    1. Compare it with the value of previous node
    ##    2. Compare it with the value of last node, if it exists
    ##    Old head node may be deleted, thus we will add a dummynode.
    ## Complexity:
    # Definition for singly-linked list.
    #class ListNode(object):
    #    def __init__(self, x):
    #        self.val = x
    #        self.next = None
    
    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if head is None:
                return None
    
            dummynode = ListNode(None)
            dummynode.next = head
            p = dummynode
            q = head
    
            previous_val = None
            while q:
                v = q.val
                if q.next and q.val == q.next.val:
                    q = q.next
                    previous_val = v
                else:
                    ## No previous node
                    if q.val == previous_val:
                        q = q.next
                        previous_val = v
                    else:
                        # add q
                        r = q.next
                        p.next = q
                        p = p.next
                        q = r
                        previous_val = v
            p.next = None
            return dummynode.next