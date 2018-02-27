# Leetcode: Binary Tree Vertical Order Traversal     :BLOG:Medium:


---

Binary Tree Vertical Order Traversal  

---

Similar Problems:  
-   [Review: Binary Tree Problems](https://brain.dennyzhang.com/review-binarytree), [Tag: #binarytree](https://brain.dennyzhang.com/tag/binarytree)

---

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).  

If two nodes are in the same row and column, the order should be from left to right.  

Examples:  

-   Given binary tree [3,9,20,null,null,15,7],

      3
     /\
    /  \
    9  20
       /\
      /  \
     15   7

return its vertical order traversal as:  

    [
      [9],
      [3,15],
      [20],
      [7]
    ]

-   Given binary tree [3,9,8,4,0,1,7],

        3
       /\
      /  \
      9   8
     /\  /\
    /  \/  \
    4  01   7

return its vertical order traversal as:  

    [
      [4],
      [9],
      [3,0,1],
      [8],
      [7]
    ]

-   Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),

        3
       /\
      /  \
      9   8
     /\  /\
    /  \/  \
    4  01   7
       /\
      /  \
      5   2

return its vertical order traversal as:  

    [
      [4],
      [9,5],
      [3,0,1],
      [8,2],
      [7]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-vertical-order-traversal)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/binary-tree-vertical-order-traversal
    ## Basic Ideas: BFS + hashmap
    ##
    ## Complexity: Time O(n), Space O(n)
    ##
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    import collections
    class Solution:
        def verticalOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if root is None: return []
            d = collections.defaultdict(lambda: [])
            queue = collections.deque([(root, 0)])
            d[0].append(root.val)
            while len(queue) != 0:
                for k in range(len(queue)):
                    (node, position) = queue.popleft()
                    if node.left:
                        d[position-1].append(node.left.val)
                        queue.append((node.left, position-1))
                    if node.right:
                        d[position+1].append(node.right.val)
                        queue.append((node.right, position+1))
            res = []
            for position in sorted(d.keys()):
                res.append(d[position])
            return res