
# Leetcode: Validate Binary Search Tree     :BLOG:Basic:

---

Basic tree datastructure  

---

Given a binary tree, determine if it is a valid binary search tree (BST).  

Assume a BST is defined as follows:  

The left subtree of a node contains only nodes with keys less than the node's key.  
The right subtree of a node contains only nodes with keys greater than the node's key.  
Both the left and right subtrees must also be binary search trees.  

    Example 1:
        2
       / \
      1   3

Binary tree [2,1,3], return true.  

    Example 2:
        1
       / \
      2   3

Binary tree [1,2,3], return false.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/validate-binary-search-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/validate-binary-search-tree/description/)  

    ## Blog link: https://code.dennyzhang.com/validate-binary-search-tree
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isValidBST(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: bool
    	"""
    	import sys
    	return self._isValidBST(root, -sys.maxsize-1, sys.maxsize)
    
        def _isValidBST(self, root, min_value, max_value):
    	if root is None:
    	    return True
    
    	if root.val <= min_value or root.val >= max_value:
    	    return False
    
    	if root.left:
    	    if self._isValidBST(root.left, min_value, root.val) is False:
    		return False
    
    	if root.right:
    	    if self._isValidBST(root.right, root.val, max_value) is False:
    		return False
    
    	return True
    
        def isValidBST_v1(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: bool
    	"""
    	## Idea: DFS recursive
    	## Complexity: Time O(n), Space O(log(n))
    	list_value = self.getBST(root)
    	for i in range(0, len(list_value)-1):
    	    if list_value[i+1] <= list_value[i]:
    		return False
    	return True
    
        def getBST(self, root):
    	if root is None:
    	    return []
    
    	res = []
    	if root.left:
    	    res += self.getBST(root.left)
    
    	res.append(root.val)
    
    	if root.right:
    	    res += self.getBST(root.right)
    	return res

