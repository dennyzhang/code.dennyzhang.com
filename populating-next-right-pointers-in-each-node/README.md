# Leetcode: Populating Next Right Pointers in Each Node     :BLOG:Medium:


---

Populating Next Right Pointers in Each Node  

---

Given a binary tree  

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.  

Initially, all next pointers are set to NULL.  

Note:  
-   You may only use constant extra space.
-   You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

    For example,
    Given the following perfect binary tree,
             1
           /  \
          2    3
         / \  / \
        4  5  6  7
    After calling your function, the tree should look like:
             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \  / \
        4->5->6->7 -> NULL

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/populating-next-right-pointers-in-each-node)  

Credits To: [Leetcode.com](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/)  

Leave me comments, if you know how to solve.  

    # Definition for binary tree with next pointer.
    # class TreeLinkNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    #         self.next = None
    
    class Solution:
        # @param root, a tree link node
        # @return nothing
        def connect(self, root):