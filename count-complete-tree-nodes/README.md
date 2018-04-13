# Leetcode: Count Complete Tree Nodes     :BLOG:Hard:


---

Count Complete Tree Nodes  

---

Similar Problems:  
-   [Review: Recursive Problems](https://code.dennyzhang.com/review-recursive), [Tag: #recursive](https://code.dennyzhang.com/tag/recursive)

---

Given a complete binary tree, count the number of nodes.  

Definition of a complete binary tree from [Wikipedia](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees):  
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/count-complete-tree-nodes)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-complete-tree-nodes/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/count-complete-tree-nodes
    ## Basic Ideas: Cut the examine dataset into half
    ##              Check height of sub-tree and right-tree
    ##              For each divide-conquer, one half will be solved without recursive
    ##
    ##    Sample Data: 
    ##             1        
    ##           /   \
    ##          2     3
    ##         /
    ##        4
    ##
    ## Complexity: Time O(h*log(n)) = O(log(n)*log(n)). Space O(1). If include system stack, Space O(log(n))
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countNodes(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0
    
            # root node is with height 0
            lh, rh = 0, 0
            lnode, rnode = root, root
            while lnode:
                lnode = lnode.left
                lh += 1
            while rnode:
                rnode = rnode.right
                rh += 1
    
            if lh == rh:
                return pow(2, lh) - 1
            else:
                return self.countNodes(root.left) + self.countNodes(root.right) + 1