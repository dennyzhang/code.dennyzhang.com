# Leetcode: All Nodes Distance K in Binary Tree     :BLOG:Medium:


---

All Nodes Distance K in Binary Tree  

---

Similar Problems:  

-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#bfs](https://code.dennyzhang.com/tag/bfs)

---

We are given a binary tree (with root node root), a target node, and an integer value \`K\`.  

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.  

Example 1:  

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
    Output: [7,4,1]
    Explanation: 
    The nodes that are a distance 2 from the target node (with value 5)
    have values 7, 4, and 1.
    
    Note that the inputs "root" and "target" are actually TreeNodes.
    The descriptions of the inputs above are just serializations of these objects.

[![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/tree_distance.png)](Leetcode: All Nodes Distance K in Binary Tree)  

Note:  

1.  The given tree is non-empty.
2.  Each node in the tree has unique values 0 <= node.val <= 500.
3.  The target node is a node in the tree.
4.  0 <= K <= 1000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/all-nodes-distance-k-in-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/all-nodes-distance-k-in-binary-tree
    // Basic Ideas: hashmap + BFS
    // Change tree to a map, then BFS
    // Complexity: Time O(n), Space O(n)
    /**
     * Definition for a binary tree node.
     * type TreeNode struct {
     *     Val int
     *     Left *TreeNode
     *     Right *TreeNode
     * }
     */
    type GraphNode struct {
        node *TreeNode
        parent *TreeNode
    }
    func distanceK(root *TreeNode, target *TreeNode, K int) int {
        m := map[int]*TreeNode{}
        queue := *TreeNode{root}
        for len(queue) != 0 {
            l := *TreeNode{}
            for _, node := range queue {
                if node.Left != nil {
                    m[node.Left.Val] = node
                    l = append(l, node.Left)
                }
                if node.Right != nil {
                    m[node.Right.Val] = node
                    l = append(l, node.Right)
                }
            }
            queue = l
        }
    
        level := 0
        var parent *TreeNode
        queue2 := *GraphNode{&GraphNode{target, nil}}
        for len(queue2) != 0 && level != K {
            l := *GraphNode{}
            for _, graphNode := range queue2 {
                node := graphNode.node
                if node.Left != nil && node.Left != graphNode.parent  {
                    l = append(l, &GraphNode{node.Left, node})
                }
                if node.Right != nil && node.Right != graphNode.parent {
                    l = append(l, &GraphNode{node.Right, node})
                }
                parent = m[node.Val]
                if parent != nil && parent != graphNode.parent {
                    l = append(l, &GraphNode{parent, node})
                }
            }
            queue2 = l
            level++
        }
        res := int{}
        for _, graphNode := range queue2 {
            res = append(res, graphNode.node.Val)
        }
        return res
    }