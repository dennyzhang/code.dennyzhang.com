
# Leetcode: Convert Binary Search Tree to Sorted Doubly Linked List     :BLOG:Medium:

---

Convert Binary Search Tree to Sorted Doubly Linked List  

---

Similar Problems:  

-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist)
-   [Review: Tree Traversal Problems](https://code.dennyzhang.com/review-treetraversal)
-   Tag: [#linkedlist](https://code.dennyzhang.com/tag/linkedlist), [#classic](https://code.dennyzhang.com/tag/classic), [#treetraversal](https://code.dennyzhang.com/tag/treetraversal)

---

Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.  

Let's take the following BST as an example, it may help you understand the problem better:  

[https://raw.githubusercontent.com/dennyzhang/challenges-leetcode-interesting/master/images/BSTDLLOriginalBST.png](Leetcode: Convert Binary Search Tree to Sorted Doubly Linked List)  

We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.  

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.  

[https://raw.githubusercontent.com/dennyzhang/challenges-leetcode-interesting/master/images/BSTDLLReturnDLL.png](Leetcode: Convert Binary Search Tree to Sorted Doubly Linked List)  

Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.  

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.  

[https://raw.githubusercontent.com/dennyzhang/challenges-leetcode-interesting/master/images/BSTDLLReturnBST.png](Leetcode: Convert Binary Search Tree to Sorted Doubly Linked List)  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/convert-binary-search-tree-to-sorted-doubly-linked-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    ## Blog link: https://code.dennyzhang.com/convert-binary-search-tree-to-sorted-doubly-linked-list
    ## Basic Ideas: dfs in-order
    ## Need to do it in-place
    ## f(node) head, tail
    ## Complexity: 
    """
    # Definition for a Node.
    class Node:
        def __init__(self, val, left, right):
            self.val = val
            self.left = left
            self.right = right
    """
    class Solution:
        def convert(self, root):
            # empty
            if root is None: return (None, None)
            # leaf
            if root.left is None and root.right is None:
                return (root, root)
    
            # in-order traversal
            head, tail = root, root
            (h1, t1) = self.convert(root.left)
            if h1: head = h1
            if t1:
                t1.next = root
                root.left = t1
    
            (h2, t2) = self.convert(root.right)
            if t2: tail = t2
            if h2:
                h2.left = root
                root.right = h2
            return (head, tail)
    
        def treeToDoublyList(self, root):
            """
            :type root: Node
            :rtype: Node
            """
            (head, _) = self.convert(root)
            return head

