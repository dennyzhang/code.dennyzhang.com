
# Leetcode: Binary Tree Longest Consecutive Sequence     :BLOG:Medium:

---

Binary Tree Longest Consecutive Sequence  

---

Similar Problems:  

-   [Leetcode: Binary Tree Longest Consecutive Sequence II](https://code.dennyzhang.com/binary-tree-longest-consecutive-sequence-ii)
-   Tag: [#binarytree](https://code.dennyzhang.com/tag/binarytree), [#treetraversal](https://code.dennyzhang.com/tag/treetraversal), [#classic](https://code.dennyzhang.com/tag/classic)

---

Given a binary tree, find the length of the longest consecutive sequence path.  

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).  

Example 1:  

    Input:
    
       1
        \
         3
        / \
       2   4
            \
             5
    
    Output: 3
    
    Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:  

    Input:
    
       2
        \
         3
        / 
       2    
      / 
     1
    
    Output: 2 
    
    Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-longest-consecutive-sequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/binary-tree-longest-consecutive-sequence
    // Basic Ideas: pre-order
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
    func preOrder(root *TreeNode, maxCnt *int) int {
        if root == nil { return 0 }
        res := 1
        var count int
        if root.Left != nil {
    	count = 1
    	v := preOrder(root.Left, maxCnt)
    	if root.Val + 1 == root.Left.Val {  count = v + 1 }
    	if count > res { res = count }
        }
        if root.Right != nil {
    	count = 1
    	v := preOrder(root.Right, maxCnt)
    	if root.Val + 1 == root.Right.Val {  count = v + 1 }
    	if count > res { res = count }
        }
        if res > *maxCnt { *maxCnt = res }
        return res
    }
    
    func longestConsecutive(root *TreeNode) int {
        maxCnt := 0
        preOrder(root, &maxCnt)
        return maxCnt
    }

