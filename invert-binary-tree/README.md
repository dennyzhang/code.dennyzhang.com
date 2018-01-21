# Leetcode: Invert Binary Tree     :BLOG:Basic:


---

Invert Binary Tree  

---

    Invert a binary tree.
         4
       /   \
      2     7
     / \   / \
    1   3 6   9

to  

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/invert-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/invert-binary-tree/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/invert-binary-tree
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def invertTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            ## Idea: BFS
            ## Complexity:
            if root is None:
                return root
            queue = []
            queue.append(root)
            while len(queue) != 0:
                element = queue.pop()
                p = element.left
                element.left = element.right
                element.right = p
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            return root
    
        def invertTree_v1(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if root is None:
                return None
            if (root.left is None) and (root.right is None):
                return root
    
            if (root.left is None) and root.right:
                root.left = self.invertTree(root.right)
                root.right = None
                return root
    
            if (root.right is None) and root.left:
                root.right = self.invertTree(root.left)
                root.left = None
                return root
    
            p = self.invertTree(root.left)
            q = self.invertTree(root.right)
            root.left = q
            root.right = p
            return root