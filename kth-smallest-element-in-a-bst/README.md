# Leetcode: Kth Smallest Element in a BST     :BLOG:Medium:


---

Identity number which appears exactly once.  

---

Similar Problems:  
-   Tag: [#classic](https://brain.dennyzhang.com/tag/classic)

---

Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/kth-smallest-element-in-a-bst)  

Credits To: [leetcode.com](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/kth-smallest-element-in-a-bst
    ## Basic Ideas: In-order trasversal
    ## Complexity: O(k), Space O(k)
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        def kthSmallest(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """
            (quota, val) = self.inorderVisit(root, k)
            # quota must be 0, since k is valid.
            return val
    
        def inorderVisit(self, root, k):
            if k == 0: return (0, None)
            if root is None: return (k, None)
    
            quota, val = k, root.val
            if root.left:
                (quota, val) = self.inorderVisit(root.left, quota)
            if quota == 0: return (0, val)
            if quota == 1: return (0, root.val)
            quota -= 1
            if root.right:
                (quota, val) = self.inorderVisit(root.right, quota)
            return (quota, val)