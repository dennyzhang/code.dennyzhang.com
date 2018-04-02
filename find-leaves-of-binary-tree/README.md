# Leetcode: Find Leaves of Binary Tree     :BLOG:Medium:


---

Find Leaves of Binary Tree  

---

Similar Problems:  
-   [Binary Tree Vertical Order Traversal](https://brain.dennyzhang.com/binary-tree-vertical-order-traversal)
-   [Review: Binary Tree Problems](https://brain.dennyzhang.com/review-binarytree), [Tag: #binarytree](https://brain.dennyzhang.com/tag/binarytree)

---

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.  

Example:  

    Given binary tree 
              1
             / \
            2   3
           / \     
          4   5    
    Returns [4, 5, 3], [2], [1].

Explanation:  

    1. Removing the leaves [4, 5, 3] would result in this tree:
              1
             / 
            2

    2. Now removing the leaf [2] would result in this tree:
              1

    3. Now removing the leaf [1] would result in the empty tree:
              []         
    Returns [4, 5, 3], [2], [1].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-leaves-of-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-leaves-of-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/find-leaves-of-binary-tree
    ## Basic Ideas: hashmap + post-order + reversed BFS
    ##
    ##  Children find out parent
    ##
    ##  Reversed BFS
    ##   1. Use post-order to initialize queue
    ##   2. Visit current layer in the queue
    ##      Decrease the child count of the parent node by 1
    ##      If the child count of parent node is 0, 
    ##          put them into the queue as the next layer
    ##
    ## Complexity: Time O(n), Space O(n)
    ##
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        def findLeaves(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            import collections
            d = collections.defaultdict(lambda:[0, None])
            queue = collections.deque()
            def helper(node):
                if node is None: return
                child_count = 0
                if node.left:
                    child_count +=1
                    d[node.left][1] = node
                    helper(node.left)
                if node.right:
                    child_count += 1
                    d[node.right][1] = node
                    helper(node.right)
                d[node][0] = child_count
                if child_count == 0:
                    queue.append(node)
    
            # initialize queue and dictionary
            helper(root)
            res = []
            # reversed BFS
            while len(queue) != 0:
                nodes = []
                for k in range(len(queue)):
                    node = queue.popleft()
                    nodes.append(node.val)
                    parent = d[node][1]
                    d[parent][0] -= 1
                    # Identity the next candidates
                    if d[parent][0] == 0: queue.append(parent)
                res.append(nodes)
            return res