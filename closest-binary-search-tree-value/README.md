# Leetcode: Closest Binary Search Tree Value     :BLOG:Basic:


---

Closest Binary Search Tree Value  

---

Similar Problems:  
-   [Closest Binary Search Tree Value II](https://brain.dennyzhang.com/closest-binary-search-tree-value-ii)
-   [Review: Binary Tree Problems](https://brain.dennyzhang.com/review-binarytree)
-   [Review: Recursive Problems](https://brain.dennyzhang.com/review-recursive)

---

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.  

Note:  
Given target value is a floating point.  
You are guaranteed to have only one unique value in the BST that is closest to the target.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/closest-binary-search-tree-value)  

Credits To: [leetcode.com](https://leetcode.com/problems/closest-binary-search-tree-value/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/closest-binary-search-tree-value
    ## Basic Ideas:
    ##    If the exact match, return
    ##    If current node is bigger than the target, we get a starting value.
    ##        Then check left sub-tree
    ##    If smaller, get a starting value. Then check right sub-tree
    ##
    ## Complexity: Time O(log(n)), Space O(1)
    ##
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        def closestValue(self, root, target):
            """
            :type root: TreeNode
            :type target: float
            :rtype: int
            """
            if root is None: return None
            res = root.val
            min_diff = abs(target - root.val)
            if min_diff == 0: return res
            check_left, check_right = False, False
            if root.val > target:
                # no need to explore the right
                check_left = True
            else:
                check_right = True
    
            if check_left and root.left:
                l_closest = self.closestValue(root.left, target)
                if abs(target - l_closest) < min_diff:
                    res = l_closest
    
            if check_right and root.right:
                r_closest = self.closestValue(root.right, target)
                if abs(target - r_closest) < min_diff:
                    res = r_closest
    
            return res