# Leetcode: Binary Tree Paths     :BLOG:Medium:


---

Given a binary tree, return all root-to-leaf paths.  

---

Given a binary tree, return all root-to-leaf paths.  

    For example, given the following binary tree:
       1
     /   \
    2     3
     \
      5
    All root-to-leaf paths are:
    
    ["1->2->5", "1->3"]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-paths)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-paths/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/binary-tree-paths
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def binaryTreePaths(self, root):
            """
            :type root: TreeNode
            :rtype: List[str]
            """
            ## Idea: DFS recursive
            ## Complexity:
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [str(root.val)]
    
            res = []
            if root.left:
                for string in self.binaryTreePaths(root.left):
                    res.append("%s->%s" % (str(root.val), string))
    
            if root.right:
                for string in self.binaryTreePaths(root.right):
                    res.append("%s->%s" % (str(root.val), string))
    
            return res