# Leetcode: Binary Tree Right Side View     :BLOG:Medium:


---

Binary Tree Right Side View  

---

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.  

    For example:
    Given the following binary tree,
       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    You should return [1, 3, 4].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-right-side-view)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-right-side-view/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/binary-tree-right-side-view
    ## Basic Ideas:
    ##        Level order traversal. And get the right most for each level
    ##                1
    ##              /   \
    ##             2     3
    ##            /
    ##           4
    ##        return: 1, 3, 4
    ## Complexity:
    ##        Time O(k), Space O(k). k is the height of the tree
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rightSideView(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if root is None:
                return []
            res = []
            queue = []
            queue.append(root)
            while len(queue) != 0:
                length = len(queue)
                for i in xrange(length):
                    element = queue[0]
                    del queue[0]
                    if element.left:
                        queue.append(element.left)
                    if element.right:
                        queue.append(element.right)
                    # right most element
                    if i == length - 1:
                        res.append(element.val)
            return res