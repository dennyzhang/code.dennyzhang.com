# Leetcode: Binary Tree Upside Down     :BLOG:Basic:


---

Binary Tree Upside Down  

---

Similar Problems:  
-   [Review: Binary Tree Problems](https://brain.dennyzhang.com/review-binarytree)

---

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.  

For example:  

    Given a binary tree {1,2,3,4,5},
        1
       / \
      2   3
     / \
    4   5

return the root of the binary tree [4,5,2,#,#,3,1].  

      4
     / \
    5   2
       / \
      3   1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-upside-down)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-upside-down/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/binary-tree-upside-down
    ## Basic Ideas: In-order
    ##
    ## Complexity: Time O(n), Space O(h). h = height of the tree
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def upsideDownBinaryTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if root is None: return None
            stack = []
            p = root
            while p:
                stack.append(p)
                p = p.left
            newRoot = stack.pop(-1)
            q = newRoot
            while len(stack) != 0:
                pre_parent = stack.pop(-1)
                q.left = pre_parent.right
                q.right = pre_parent
                q = pre_parent
            # configure the last node as a leaf
            q.left, q.right = None, None
            return newRoot