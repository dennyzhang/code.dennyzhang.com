
# Leetcode: Middle of the Linked List     :BLOG:Basic:

---

Middle of the Linked List  

---

Similar Problems:  

-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist)
-   Tag: [#linkedlist](https://code.dennyzhang.com/tag/linkedlist)

---

Given a non-empty, singly linked list with head node head, return a middle node of linked list.  

If there are two middle nodes, return the second middle node.  

Example 1:  

    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:  

    Input: [1,2,3,4,5,6]
    Output: Node 4 from this list (Serialization: [4,5,6])
    Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:  

-   The number of nodes in the given list will be between 1 and 100.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/middle-of-the-linked-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/middle-of-the-linked-list/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/middle-of-the-linked-list
    // Basic Ideas: fast-slow pointers
    // Complexity: Time O(n), Space O(1)
    /**
     * Definition for singly-linked list.
     * type ListNode struct {
     *     Val int
     *     Next *ListNode
     * }
     */
    func middleNode(head *ListNode) *ListNode {
        if head == nil { return nil }
        f, s := head, head
        // last node
        for f != nil && f.Next != nil {
    	s = s.Next
    	f = f.Next.Next
        }
        return s
    }

