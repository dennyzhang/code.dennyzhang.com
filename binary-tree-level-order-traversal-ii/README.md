# Leetcode: Binary Tree Level Order Traversal II     :BLOG:Medium:


---

Binary Tree Level Order Traversal II  

---

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).  

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-level-order-traversal-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/binary-tree-level-order-traversal-ii
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def levelOrderBottom(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            ## Idea: BFS
            ## Complexity:
            res = []
            if root is None:
                return res
            queue = []
            queue.append(root)
            while len(queue) != 0:
                length = len(queue)
                l = []
                for i in xrange(length):
                    l.append(queue[i].val)
                res.insert(0, l)
    
                for i in xrange(length):
                    element = queue[0]
                    del queue[0]
                    if element.left:
                        queue.append(element.left)
                    if element.right:
                        queue.append(element.right)
            return res