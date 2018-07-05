# Leetcode: Binary Tree Maximum Path Sum     :BLOG:Medium:


---

Binary Tree Maximum Path Sum  

---

Given a binary tree, find the maximum path sum.  

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.  

    For example:
    Given the below binary tree,
    
           1
          / \
         2   3
    Return 6.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-maximum-path-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/binary-tree-maximum-path-sum
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def maxPathSum(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """