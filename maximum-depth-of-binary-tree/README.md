# Leetcode: Maximum Depth of Binary Tree     :BLOG:Basic:


---

Given a binary tree, find its maximum depth.  

---

Given a binary tree, find its maximum depth.  

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximum-depth-of-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/maximum-depth-of-binary-tree
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def maxDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            ## Idea: DFS
            ## Complexity:
            depth = None
            if root is None:
                return 0
            if (root.left is None) and (root.right is None):
                return 1
            elif (root.left is None):
                return self.maxDepth(root.right)+1
            elif (root.right is None):
                return self.maxDepth(root.left)+1
            else:
                return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)