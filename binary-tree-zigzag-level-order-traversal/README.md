# Leetcode: Binary Tree Zigzag Level Order Traversal     :BLOG:Amusing:


---

Binary Tree Zigzag Level Order Traversal  

---

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).  

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-zigzag-level-order-traversal)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/binary-tree-zigzag-level-order-traversal
    ## Basic Ideas: BFS, use left_to_right(boolen) for level traversal direction
    ## Complexity: Time O(n), Space O(k)
    
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def zigzagLevelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if root is None:
                return []
            res = []
            queue = []
            queue.append(root)
            left_to_right = True
            while len(queue) != 0:
                length = len(queue)
                level_element = []
                for i in xrange(length):
                    element = queue[0]
                    del queue[0]
                    if left_to_right is True:
                        level_element.append(element.val)
                    else:
                        level_element.insert(0, element.val)
                    if element.left:
                        queue.append(element.left)
                    if element.right:
                        queue.append(element.right)
                res.append(level_element)
                left_to_right = not left_to_right
            return res