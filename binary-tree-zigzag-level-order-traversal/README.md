# Leetcode: Binary Tree Zigzag Level Order Traversal     :BLOG:Amusing:


---

Binary Tree Zigzag Level Order Traversal  

---

Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/majority-element-ii)  

Credits To: [Leetcode.com](https://leetcode.com/problems/majority-element-ii/description/)  

Leave me comments, if you know how to solve.  

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
                return 
            res = 
            queue = 
            queue.append(root)
            left_to_right = True
            while len(queue) != 0:
                length = len(queue)
                level_element = 
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