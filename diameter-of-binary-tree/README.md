# Leetcode: Diameter of Binary Tree     :BLOG:Amusing:


---

Diameter of Binary Tree  

---

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.  

    Example:
    Given a binary tree 
              1
             / \
            2   3
           / \     
          4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].  

Note: The length of path between two nodes is represented by the number of edges between them.  

Blog link: <http://brain.dennyzhang.com/diameter-of-binary-tree>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def diameterOfBinaryTree(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            ## Ideas: max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.rigt), pass_root)
            (diameter, _depth) = self._diameterOfBinaryTree(root)
            return diameter
    
        def _diameterOfBinaryTree(self, root):
            """
            :type root: TreeNode
            :rtype: (_diameterOfBinaryTree, max_depth)
            """
            if root is None:
                return (0, 0)
    
            if root.left is None and root.right is None:
                return (0, 1)
    
            res_diameter, res_depth = 0, 0
            left_diameter, left_depth = 0, 0
            right_diameter, right_depth = 0, 0
    
            if root.left:
                (left_diameter, left_depth) = self._diameterOfBinaryTree(root.left)
            if root.right:
                (right_diameter, right_depth) = self._diameterOfBinaryTree(root.right)
    
            res_depth = max(left_depth, right_depth) + 1
            res_diameter = max(left_diameter, right_diameter, left_depth+right_depth)
            return (res_diameter, res_depth)