# Leetcode: Recover Binary Search Tree     :BLOG:Medium:


---

Recover Binary Search Tree  

---

Two elements of a binary search tree (BST) are swapped by mistake.  

Recover the tree without changing its structure.  

Note:  
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?  

Blog link: <http://brain.dennyzhang.com/recover-binary-search-tree>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/recover-binary-search-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/recover-binary-search-tree/description)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas:
    ##              It could be left-right swap or parent-child swap
    ##              It could also be two non-adjacent nodes
    ##              Identity the node. Then swap the value
    ##  Assumption: Whether the tree contains duplicates?
    ## Complexity:
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def recoverTree(self, root):
            """
            :type root: TreeNode
            :rtype: void Do not return anything, modify root in-place instead.
            """
            if root is None:
                return
            # level tree trasversal
            queue = 
            queue.append(root)
            while len(queue) != 0:
                for i in xrange(len(queue)):
                    node = queue[0]
                    del queue[0]
                    # issue of left-right
                    if node.left and node.right and node.left.val > node.right.val:
                        node.left.val, node.right.val = node.right.val, node.left.val
                        return
                    # issue of parent-child
                    if node.left and node.val < node.left.val:
                        node.val, node.left.val = node.left.val, node.val
                        return
                    if node.right and node.val > node.right.val:
                        node.val, node.right.val = node.right.val, node.val
                        return
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)