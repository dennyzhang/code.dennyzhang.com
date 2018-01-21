# Leetcode: Delete Node in a BST     :BLOG:Medium:


---

Delete Node in a BST  

---

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.  

Basically, the deletion can be divided into two stages:  

1.  Search for a node to remove.
2.  If the node is found, delete the node.

Note: Time complexity should be O(height of tree).  

    Example:
    
    root = [5,3,6,2,4,null,7]
    key = 3
    
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Given key to delete is 3. So we find the node with value 3 and delete it.
    
    One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
    
        5
       / \
      4   6
     /     \
    2       7
    
    Another valid answer is [5,2,6,null,4,null,7].
    
        5
       / \
      2   6
       \   \
        4   7

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/delete-node-in-a-bst)  

Credits To: [leetcode.com](https://leetcode.com/problems/delete-node-in-a-bst/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Find the target
    ##              If the target is a leaf, we need the parent node
    ##              If the target only have one child
    ##              If the target has both children
    ##
    ## Complexity: Time O(h), Space O(1)
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def deleteNode(self, root, key):
            """
            :type root: TreeNode
            :type key: int
            :rtype: TreeNode
            """
            if root is None:
                return None
    
            # delete root
            if root.val == key:
                # root is a leaf
                if root.left is None and root.right is None:
                    return None
                else:
                    self.deleteRootNode(root, None)
                    return root
    
            # delete node inside the tree
            prev, node = root, root
            while node:
                if node.val == key:
                    break
                prev = node
                if node.val > key:
                    node = node.left
                else:
                    node = node.right
    
            # node is the target to be deleted
            if node:
                self.deleteRootNode(node, prev)
            return root
    
        def deleteRootNode(self, root, prev):
            if root is None:
                return
            # leaf
            if root.left is None and root.right is None:
                if root == prev.left:
                    prev.left = None
                else:
                    prev.right = None
                return
            if root.left:
                # find the largest item in the left right
                p, node = root, root.left
                while node.right:
                    p = node
                    node = node.right
                # swap value
                root.val = node.val
                return self.deleteRootNode(node, p)
            if root.right:
                p, node = root, root.right
                while node.left:
                    p = node
                    node = node.left
                root.val = node.val
                return self.deleteRootNode(node, p)