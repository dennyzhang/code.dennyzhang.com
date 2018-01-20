# Leetcode: Convert Sorted Array to Binary Search Tree     :BLOG:Basic:


---

Convert Sorted Array to Binary Search Tree  

---

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.  

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.  

Example:  

    Given the sorted array: [-10,-3,0,5,9],
    
    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
    
          0
         / \
       -3   9
       /   /
     -10  5

Blog link: <http://brain.dennyzhang.com/convert-sorted-array-to-binary-search-tree>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/convert-sorted-array-to-binary-search-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Find the middle node
    ## Complexity: Time O(n), Space O(1)
    
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sortedArrayToBST(self, nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            length = len(nums)
            if length == 0:
                return None
            mid_index = length/2
            head = TreeNode(nums[mid_index])
            head.left = self.sortedArrayToBST(nums[0:mid_index])
            head.right = self.sortedArrayToBST(nums[mid_index+1:])
            return head