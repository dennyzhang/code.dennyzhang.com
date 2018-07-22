
# Leetcode: N-ary Tree Preorder Traversal     :BLOG:Basic:

---

N-ary Tree Preorder Traversal  

---

Similar Problems:  

-   [Review: Tree Traversal Problems](https://code.dennyzhang.com/review-treetraversal)
-   Tag: [#treetraversal](https://code.dennyzhang.com/tag/treetraversal), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given an n-ary tree, return the preorder traversal of its nodes' values.  

For example, given a 3-ary tree:  

[![img](https://raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/NaryTreeExample.png)](Leetcode: N-ary Tree Postorder Traversal)  

Return its preorder traversal as: [1,3,5,6,2,4].  

Note: Recursive solution is trivial, could you do it iteratively?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/n-ary-tree-preorder-traversal)  

Credits To: [leetcode.com](https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: recursive

    ## Blog link: https://code.dennyzhang.com/n-ary-tree-preorder-traversal
    ## Basic Ideas:
    ##
    ## Complexity:
    """
    # Definition for a Node.
    class Node(object):
        def __init__(self, val, children):
            self.val = val
            self.children = children
    """
    class Solution(object):
        def preorder(self, root):
            """
            :type root: Node
            :rtype: List[int]
            """
            if root is None: return 
            res = [root.val]
            for child in root.children:
                res += self.preorder(child)
            return res

