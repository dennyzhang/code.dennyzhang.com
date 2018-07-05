# Leetcode: Inorder Successor in BST     :BLOG:Medium:


---

Inorder Successor in BST  

---

Similar Problems:  
-   Tag: [#treetraversal](https://code.dennyzhang.com/tag/treetraversal), [#classic](https://code.dennyzhang.com/tag/classic)

---

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.  

Note: If the given node has no in-order successor in the tree, return null.  

Example 1:  

    Input: root = [2,1,3], p = 1
    
      2
     / \
    1   3
    
    Output: 2

Example 2:  

    Input: root = [5,3,6,2,4,null,null,1], p = 6
    
          5
         / \
        3   6
       / \
      2   4
     /   
    1
    
    Output: null

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/inorder-successor-in-bst)  

Credits To: [leetcode.com](https://leetcode.com/problems/inorder-successor-in-bst/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

Intuitive Idea would have too many details.  

    ## If p has right child, we can easily find the target in its sub-tree
    ## Otherwise: Use DFS to find all parents of p, from root down to p
    ##    If p is the left-subtree of q, q is the target
    ##    Otherwise keep looking up. If we get the root, return null
    ##

    ## Blog link: https://code.dennyzhang.com/inorder-successor-in-bst
    ## Basic Ideas:
    ## 
    ## Complexity:
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def inorderSuccessor(self, root, p):
            """
            :type root: TreeNode
            :type p: TreeNode
            :rtype: TreeNode
            """
            if p is None or root is None: return None
            res = None
            while root:
                if root.val > p.val:
                    # go to left
                    res = root
                    root = root.left
                else:
                    # go to right
                    root = root.right
            return res