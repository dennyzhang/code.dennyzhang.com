# Leetcode: Subtree of Another Tree     :BLOG:Amusing:


---

Subtree of Another Tree  

---

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.  

    Example 1:
    Given tree s:
    
         3
        / \
       4   5
      / \
     1   2
    Given tree t:
       4 
      / \
     1   2
    Return true, because t has the same structure and node values with a subtree of s.

    Example 2:
    Given tree s:
    
         3
        / \
       4   5
      / \
     1   2
        /
       0
    Given tree t:
       4
      / \
     1   2
    Return false.

Blog link: <http://brain.dennyzhang.com/subtree-of-another-tree>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/subtree-of-another-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/subtree-of-another-tree/description)  

Leave me comments, if you know how to solve.  

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isSubtree(self, s, t):
            """
            :type s: TreeNode
            :type t: TreeNode
            :rtype: bool
            """