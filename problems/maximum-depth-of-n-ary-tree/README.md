
# Leetcode: Maximum Depth of N-ary Tree     :BLOG:Basic:

---

Maximum Depth of N-ary Tree  

---

Similar Problems:  

-   [Review: Tree Traversal Problems](https://code.dennyzhang.com/review-treetraversal)
-   Tag: [#treetraversal](https://code.dennyzhang.com/tag/treetraversal), [#recursive](https://code.dennyzhang.com/tag/recursive), [#dfs](https://code.dennyzhang.com/tag/dfs), [#bfs](https://code.dennyzhang.com/tag/bfs)

---

Given a n-ary tree, find its maximum depth.  

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.  

For example, given a 3-ary tree:  

[![img](https://raw.githubusercontent.com/dennyzhang/challenges-leetcode-interesting/master/images/NaryTreeExample.png)](Leetcode: N-ary Tree Postorder Traversal)  

We should return its max depth, which is 3.  

Note:  

The depth of the tree is at most 1000.  
The total number of nodes is at most 5000.  

Credits To: [leetcode.com](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: recursive

    ## Blog link: https://code.dennyzhang.com/maximum-depth-of-n-ary-tree
    ## Basic Ideas: recursive
    ##
    ## Complexity: Time O(n), Space O(n)
    
    """
    # Definition for a Node.
    class Node(object):
        def __init__(self, val, children):
            self.val = val
            self.children = children
    """
    class Solution(object):
        def maxDepth(self, root):
            """
            :type root: Node
            :rtype: int
            """
            if root is None: return 0
            max_height = 0
            for child in root.children:
                max_height = max(max_height, self.maxDepth(child))
            return max_height+1

