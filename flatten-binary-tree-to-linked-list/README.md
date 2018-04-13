# Leetcode: Flatten Binary Tree to Linked List     :BLOG:Basic:


---

Flatten Binary Tree to Linked List  

---

Given a binary tree, flatten it to a linked list in-place.  

    For example,
    Given
    
             1
            / \
           2   5
          / \   \
         3   4   6

    The flattened tree should look like:
       1
        \
         2
          \
           3
            \
             4
              \
               5
                \
                 6

Hints:  

If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/flatten-binary-tree-to-linked-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/flatten-binary-tree-to-linked-list
    ## Basic Ideas: DFS for pre-order traversal
    ## Complexity: Time O(n), Space O(n)
    
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def flatten(self, root):
            """
            :type root: TreeNode
            :rtype: void Do not return anything, modify root in-place instead.
            """
            self._flatten(root)
    
        def _flatten(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode: last node in the chain
            """
            if root is None:
                return None
            if root.left is None and root.right is None:
                return root
    
            root_right = root.right
            q = None
            if root.left:
                q = self._flatten(root.left)
                q.right = root.right
                root.right = root.left
                root.left = None
    
            if root_right:
                q = self._flatten(root.right)
    
            return q