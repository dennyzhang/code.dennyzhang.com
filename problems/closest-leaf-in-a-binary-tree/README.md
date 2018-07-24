
# Leetcode: Closest Leaf in a Binary Tree     :BLOG:Medium:

---

Closest Leaf in a Binary Tree  

---

Similar Problems:  

-   Tag: [#treetraversal](https://code.dennyzhang.com/tag/treetraversal), [#bfs](https://code.dennyzhang.com/tag/bfs),[#inspiring](https://code.dennyzhang.com/tag/inspiring), [#classic](https://code.dennyzhang.com/tag/classic)

---

Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.  

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.  

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.  

Example 1:  

    Input:
    root = [1, 3, 2], k = 1
    Diagram of binary tree:
              1
             / \
            3   2
    
    Output: 2 (or 3)
    
    Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.

Example 2:  

    Input:
    root = [1], k = 1
    Output: 1
    
    Explanation: The nearest leaf node is the root node itself.

Example 3:  

    Input:
    root = [1,2,3,4,null,null,null,5,null,6], k = 2
    Diagram of binary tree:
                 1
                / \
               2   3
              /
             4
            /
           5
          /
         6
    
    Output: 3
    Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

Note:  

-   root represents a binary tree with at least 1 node and at most 1000 nodes.
-   Every node has a unique node.val in range [1, 1000].
-   There exists some node in the given binary tree for which node.val == k.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/closest-leaf-in-a-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/closest-leaf-in-a-binary-tree
    // Basic Ideas:
    // Convert tree to graph
    // Notice:
    // - We assume node with one edge as leaf. So we need special consideration for root node.
    // - When target is already a leaf, we return it directly
    //
    // Complexity: Time O(n), Space O(1)
    /**
     * Definition for a binary tree node.
     * type TreeNode struct {
     *     Val int
     *     Left *TreeNode
     *     Right *TreeNode
     * }
     */
    
    type GraphNode struct {
        cur, prev int
    }
    
    func findClosestLeaf(root *TreeNode, k int) int {
        // Need to return root
        if root.Left == nil && root.Right == nil { 
    	return root.Val 
        }
    
        m := map[int][]int{}
        queue := []*TreeNode{root}
        for len(queue) != 0 {
    	l := []*TreeNode{}
    	for _, node := range queue {
    	    if node.Left != nil {
    		m[node.Val] = append(m[node.Val], node.Left.Val)
    		m[node.Left.Val] = append(m[node.Left.Val], node.Val)
    		l = append(l, node.Left)
    	    }
    	    if node.Right != nil {
    		m[node.Val] = append(m[node.Val], node.Right.Val)
    		m[node.Right.Val] = append(m[node.Right.Val], node.Val)
    		l = append(l, node.Right)
    	    }
    	}
    	queue = l
        }
        // Need to return target
        if k != root.Val && len(m[k]) == 1 {
    	return k
        }
    
        // bfs
        queue2 := []GraphNode{GraphNode{k, -1}}
        for len(queue2) != 0 {
    	l := []GraphNode{}
    	for _, p := range queue2 {
    	    // avoid return root
    	    if p.cur != root.Val && len(m[p.cur]) == 1 {
    		return p.cur
    	    }
    	    for _, v := range m[p.cur] {
    		if v == p.prev { continue }
    		l = append(l, GraphNode{v, p.cur})
    	    }
    	}
    	queue2 = l
        }
        return -1
    }

