
# Leetcode: Binary Tree Inorder Traversal     :BLOG:Basic:

---

Binary Tree Inorder Traversal  

---

Similar Problems:  

-   Tag: [#treetraversal](https://code.dennyzhang.com/tag/treetraversal)

---

Given a binary tree, return the inorder traversal of its nodes' values.  

For example:  

    Given binary tree [1,null,2,3],
       1
        \
         2
        /
       3
    return [1,3,2].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/binary-tree-inorder-traversal)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/binary-tree-inorder-traversal
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def inorderTraversal(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: List[int]
    	"""
    	if root is None:
    	    return []
    	res = []
    	stack = []
    	p = root
    	# initialize the stack
    	while p:
    	    stack.append(p)
    	    p = p.left
    
    	# DFS
    	while(len(stack) != 0):
    	    top_item = stack.pop()
    	    res.append(top_item.val)
    	    if top_item.right:
    		p = top_item.right
    		while p:
    		    stack.append(p)
    		    p = p.left
    	return res
    
        def inorderTraversal_v1(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: List[int]
    	"""
    	l = []
    	self.inorderTraversalRec(root, l)
    	return l
    
        def inorderTraversalRec(self, root, list_value):
    	if root is None:
    	    return
    
    	if root.left is not None:
    	    self.inorderTraversalRec(root.left, list_value)
    
    	list_value.append(root.val)
    
    	if root.right is not None:
    	    self.inorderTraversalRec(root.right, list_value)

