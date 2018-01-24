# Leetcode: Copy List with Random Pointer     :BLOG:Amusing:


---

Copy List with Random Pointer  

---

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.  

Return a deep copy of the list.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/copy-list-with-random-pointer)  

Credits To: [leetcode.com](https://leetcode.com/problems/copy-list-with-random-pointer/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/copy-list-with-random-pointer
    ## Basic Ideas:
    ##            |------------|
    ##            |            v
    ##            1  --> 2 --> 3 --> 4
    ##
    ##            |--------------------------|
    ##            |                          v
    ##            1  --> 1' --> 2 --> 2' --> 3 --> 3' --> 4 --> 4'
    ##                   |                         |
    ##                   |-------------------------|
    ## Complexity: Time O(n), Space O(1)
    ##
    # Definition for singly-linked list with a random pointer.
    # class RandomListNode(object):
    #     def __init__(self, x):
    #         self.label = x
    #         self.next = None
    #         self.random = None
    
    class Solution(object):
        def copyRandomList(self, head):
            """
            :type head: RandomListNode
            :rtype: RandomListNode
            """
            if head is None:
                return None
    
            ## duplicate the list
            p = head
            while p:
                newNode = RandomListNode(p.label)
                newNode.next = p.next
                p.next = newNode
                p = newNode.next
    
            ## copy the randome pointer
            ##   odd node is the original list
            ##   even node is the new list
            p1 = head
            while p1:
                p2 = p1.next
                if p1.random:
                    p2.random = p1.random.next
                # move to next
                p1 = p1.next.next
    
            # change back the pointers
            res = head.next
            p1 = head
            while p1:
                q1 = p1.next.next
                p2 = p1.next
                p1.next = p1.next.next
                if p2.next:
                    p2.next = p2.next.next
                p1 = q1
            return res