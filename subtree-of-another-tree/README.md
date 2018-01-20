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

    ## Basic Ideas: pre-order trasversal
    ##
    ## Complexity: Time ? Space ?
    ##
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
            if t is None: return True
            if s is None: return False
            if s.val == t.val:
                if self.isSameTree(s.left, t.left) and \
                    self.isSameTree(s.right, t.right):
                    return True
    
            b1 = self.isSubtree(s.left, t)
            if b1:
                return True
            else:
                b2 = self.isSubtree(s.right, t)
                return True if b2 else False
    
        def isSameTree(self, s, t):
            if s is None or t is None:
                return (s is None) and (t is None)
            if s.val != t.val: return False
            return self.isSameTree(s.left, t.left) and \
                self.isSameTree(s.right, t.right)