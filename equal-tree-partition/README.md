# Leetcode: Equal Tree Partition     :BLOG:Medium:


---

Equal Tree Partition  

---

Similar Problems:  
-   Tag: [#binarytree](https://code.dennyzhang.com/tag/binarytree)

---

Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.  

Example 1:  

    Input:     
        5
       / \
      10 10
        /  \
       2   3
    
    Output: True
    Explanation: 
        5
       / 
      10
          
    Sum: 15
    
       10
      /  \
     2    3
    
    Sum: 15

Example 2:  

    Input:     
        1
       / \
      2  10
        /  \
       2   20
    
    Output: False
    Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.

Note:  
-   The range of tree node value is in the range of [-100000, 100000].
-   1 <= n <= 10000

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/equal-tree-partition)  

Credits To: [leetcode.com](https://leetcode.com/problems/equal-tree-partition/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/equal-tree-partition
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        ## Basic Ideas: Use set to solve it in one pass, instead of two
        ## Complexity: Time O(n), Space O(n)
        def checkEqualTree(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            def treeSum(node):
                if node is None: return 0
                res = node.val + treeSum(node.left) + treeSum(node.right)
                if node != root: values.add(res)
                return res
    
            values = set([])
            total = treeSum(root)
            return total/2 in values
    
        ## Basic Ideas: two pass
        ##   1. post-order: config the node value as the sum of all children
        ##   2. tree trasveral: if any node value is half of the total, return True
        ## Complexity: Time O(n), Space O(1)
        def checkEqualTree_v1(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            self.postVisitChange(root)
            # bfs to examine the result
            target = root.val/2
            import collections
            queue = collections.deque()
            queue.append(root)
            while len(queue) != 0:
                for k in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        if node.left.val == target: return True
                        queue.append(node.left)
                    if node.right:
                        if node.right.val == target: return True
                        queue.append(node.right)
            return False
    
        def postVisitChange(self, root):
            if root is None: return
            if root.left:
                self.postVisitChange(root.left)
            if root.right:
                self.postVisitChange(root.right)
            if root.left: root.val += root.left.val
            if root.right: root.val += root.right.val