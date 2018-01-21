# Leetcode: Two Sum IV - Input is a BST     :BLOG:Basic:


---

Two Sum IV - Input is a BST  

---

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.  

    Example 1:
    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Target = 9
    
    Output: True

    Example 2:
    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Target = 28
    
    Output: False

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/two-sum-iv-input-is-a-bst)  

Credits To: [leetcode.com](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)  

Leave me comments, if you know how to solve.  

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findTarget(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: bool
            """
            ## Idea: Generate a sorted array from binary search tree.
            ##       Use 2 sum
            ## Complexity: Time O(n), Space O(n)
            nums = self._convertBST2Array(root)
            length = len(nums)
            if length < 2:
                return False
    
            i, j = 0, length-1
            while i<j:
                sum_value = nums[i] + nums[j]
                if sum_value == k:
                    return True
                elif sum_value < k:
                    i += 1
                else:
                    j -= 1
            return False
    
        def _convertBST2Array(self, root):
            """
            :type root: TreeNode
            :rtype: list
            """
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [root.val]
    
            res = []
            if root.left:
                res = self._convertBST2Array(root.left) + res
            res = res + [root.val]
            if root.right:
                res = res + self._convertBST2Array(root.right)
            return res