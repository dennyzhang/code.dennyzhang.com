
# Leetcode: Serialize and Deserialize BST     :BLOG:Basic:

---

Serialize and Deserialize BST  

---

Similar Problems:  

-   [Serialize and Deserialize Binary Tree](https://code.dennyzhang.com/serialize-and-deserialize-binary-tree)
-   Tag: [#binarytree](https://code.dennyzhang.com/tag/binarytree)

---

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.  

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.  

The encoded string should be as compact as possible.  

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/serialize-and-deserialize-bst)  

Credits To: [leetcode.com](https://leetcode.com/problems/serialize-and-deserialize-bst/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/serialize-and-deserialize-bst
    ## Basic Ideas: Pre-order
    ## Complexity: Time O(n), Space O(n)
    ##
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Codec:
    
        def serialize(self, root):
    	"""Encodes a tree to a single string.
    
    	:type root: TreeNode
    	:rtype: str
    	"""
    	def pre_order(root):
    	    if root is None: return ""
    
    	    ret = str(root.val)
    	    left = pre_order(root.left)
    	    if left: ret = "%s %s" % (ret, left)
    
    	    right = pre_order(root.right)
    	    if right: ret = "%s %s" % (ret, right)
    	    return ret
    
    	return pre_order(root)
    
        def deserialize(self, data):
    	"""Decodes your encoded data to tree.
    
    	:type data: str
    	:rtype: TreeNode
    	"""
    	def my_deserialize(l):
    	    import sys
    	    if len(l) == 0: return None
    	    root = TreeNode(l[0])
    	    index = sys.maxsize
    	    for i in range(1, len(l)):
    		if l[i] > root.val:
    		    index = i
    		    break
    	    root.left = my_deserialize(l[1:index])
    	    root.right = my_deserialize(l[index:])
    	    return root
    
    	if data == "": return None
    	l = [int(x) for x in data.split(" ")]
    	return my_deserialize(l)        
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))

