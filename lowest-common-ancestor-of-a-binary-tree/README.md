# Leetcode: Lowest Common Ancestor of a Binary Tree     :BLOG:Basic:


---

Lowest Common Ancestor of a Binary Tree  

---

Similar Problems:  
-   [Review: Classic Code Problems](https://code.dennyzhang.com/review-classic)
-   [Lowest Common Ancestor of a Binary Search Tree](https://code.dennyzhang.com/lowest-common-ancestor-of-a-binary-search-tree)
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic), [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#recursive](https://code.dennyzhang.com/tag/recursive), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.  

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself)."  

Given the following binary search tree:  root = [3,5,1,6,2,0,8,null,null,7,4]  

         _______3______
        /              \
     ___5__          ___1__
    /      \        /      \
    6      _2       0       8
          /  \
          7   4

Example 1:  

    Input: root, p = 5, q = 1
    Output: 3
    Explanation: The LCA of of nodes 5 and 1 is 3.

Example 2:  

    Input: root, p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
                 according to the LCA definition.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/lowest-common-ancestor-of-a-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/lowest-common-ancestor-of-a-binary-tree
    ## Basic Ideas: recursive
    ##
    ## Notice:
    ##   Here we assume p, q will exists in the tree
    ##
    ## Complexity: ?
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    class Solution(object):
        def lowestCommonAncestor(self, root, p, q):
            """
            :type root: TreeNode
            :type p: TreeNode
            :type q: TreeNode
            :rtype: TreeNode
            """
            if root is None or root == p or root == q: return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left and right: return root
            return left if left else right