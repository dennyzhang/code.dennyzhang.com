
# Leetcode: Insert into a Cyclic Sorted List     :BLOG:Medium:

---

Insert into a Cyclic Sorted List  

---

Similar Problems:  

-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist)
-   Tag: [#linkedlist](https://code.dennyzhang.com/tag/linkedlist), [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.  

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.  

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.  

The following example may help you understand the problem better:  

[https://raw.githubusercontent.com/dennyzhang/challenges-leetcode-interesting/master/images/InsertCyclicAfter.png](Leetcode: Insert into a Cyclic Sorted List)  

In the figure above, there is a cyclic sorted list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list.  

[https://raw.githubusercontent.com/dennyzhang/challenges-leetcode-interesting/master/images/InsertCyclicBefore.png](Leetcode: Insert into a Cyclic Sorted List)  

The new node should insert between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/insert-into-a-cyclic-sorted-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    ## Blog link: https://code.dennyzhang.com/insert-into-a-cyclic-sorted-list
    ## Basic Ideas:
    ##    Find the smallest value which is no less than the target
    ##    If there are multiple suitable places for insertion, 
    ##      here we choose to insert into the first suitable place after head.
    ##
    ## Question: how we know we are running the loop again?
    ##
    ## Complexity: Time O(n), Space O(1)
    """
    # Definition for a Node.
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next
    """
    class Solution:
        def insert(self, head, insertVal):
            """
            :type head: Node
            :type insertVal: int
            :rtype: Node
            """
            node = Node(insertVal, None)
            # empty
            if head is None:
                node.next = node
                return node
    
            # one node
            if head.next is None:
                head.next = node
                node.next = head
                return head
    
            # find the smallest value, which is no less than the target
            p = head
            while True:
                # print("here1. insertVal: %d, p.val: %d, p.next.val: %d" % (insertVal, p.val, p.next.val))
                # end of the loop
                if p.val > p.next.val:
                    # biggest or smallest
                    if insertVal >= p.val or insertVal <= p.next.val:
                        break
    
                    # should keep going
                    if insertVal > p.next.val and insertVal < p.val:
                        p = p.next
                        continue
                    break
    
                if insertVal >= p.val and insertVal <= p.next.val:
                    break
                p = p.next
                if p == head:
                    # run into the loop again
                    break
    
            node.next = p.next
            p.next = node
            return head        

