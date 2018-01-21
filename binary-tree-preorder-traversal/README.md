# Leetcode: Binary Tree Preorder Traversal     :BLOG:Basic:


---

Binary Tree Preorder Traversal  

---

Given a binary tree, return the preorder traversal of its nodes' values.  

    For example:
    Given binary tree [1,null,2,3],
       1
        \
         2
        /
       3
    return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-preorder-traversal)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)  

Leave me comments, if you know how to solve.  

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def preorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            res = []
            stack = []
            p = root
            # Whatever I have pushed to stack, I have visited already
            while p:
                res.append(p.val)
                stack.append(p)
                p = p.left
    
            while len(stack) != 0:
                top_item = stack.pop()
                # get right
                if top_item.right:
                    p = top_item.right
                    while p:
                        res.append(p.val)
                        stack.append(p)
                        p = p.left
            return res
    
        def preorderTraversal_v1(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            res = []
            self.preorderTraversalRec(root, res)
            return res
        def preorderTraversalRec(self, root, list_value):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if root is None:
                return
            list_value.append(root.val)
            if root.left:
                self.preorderTraversalRec(root.left, list_value)
            if root.right:
                self.preorderTraversalRec(root.right, list_value)