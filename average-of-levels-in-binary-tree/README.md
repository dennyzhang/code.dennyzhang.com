# Leetcode: Average of Levels in Binary Tree     :BLOG:Medium:


---

Average of Levels in Binary Tree  

---

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.  

    Example 1:
    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]

Explanation:  
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].  
Note:  
The range of node's value is in the range of 32-bit signed integer.  

Blog link: <http://brain.dennyzhang.com/average-of-levels-in-binary-tree>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/average-of-levels-in-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/average-of-levels-in-binary-tree/description)  

Leave me comments, if you know how to solve.  

    ## Idea: BFS, Level Order Tree Traversal
    ## Complexity: Time O(n), Space O(k)
    
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def averageOfLevels(self, root):
            """
            :type root: TreeNode
            :rtype: List[float]
            """
            if root is None:
                return []
            res = []
            queue = []
            queue.append(root)
            while len(queue) != 0:
                length = len(queue)
                average_level = 0
                for i in xrange(length):
                    element = queue[0]
                    del queue[0]
                    average_level += element.val
                    if element.left:
                        queue.append(element.left)
                    if element.right:
                        queue.append(element.right)
                res.append(float(average_level)/length)
            return res