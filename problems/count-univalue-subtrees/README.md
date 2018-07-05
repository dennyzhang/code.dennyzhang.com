
# Leetcode: Count Univalue Subtrees     :BLOG:Medium:

---

Count Univalue Subtrees  

---

Similar Problems:  

-   Tag: [#treetraversal](https://code.dennyzhang.com/tag/treetraversal)

---

Given a binary tree, count the number of uni-value subtrees.  

A Uni-value subtree means all nodes of the subtree have the same value.  

Example :  

    Input:  root = [5,1,5,5,5,null,5]
    
                  5
                 / \
                1   5
               / \   \
              5   5   5
    
    Output: 4

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/count-univalue-subtrees)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-univalue-subtrees/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: post-order with null and leaf as corner cases

    // Blog link: https://code.dennyzhang.com/count-univalue-subtrees
    // Basic Ideas: post-order
    // Complexity: Time O(n), Space O(1)
    /**
     * Definition for a binary tree node.
     * type TreeNode struct {
     *     Val int
     *     Left *TreeNode
     *     Right *TreeNode
     * }
     */
    var count int
    func postOrder(root *TreeNode) bool {
        if root == nil { return false }
        if root.Left == nil && root.Right == nil { 
    	count++
    	return true
        }
        s1, s2 := true, true
        if (root.Left != nil) { 
    	s1 = postOrder(root.Left)
    	if root.Left.Val != root.Val { s1 = false }
        }
        if (root.Right != nil) { 
    	s2 = postOrder(root.Right) 
    	if root.Right.Val != root.Val { s2 = false }
        }
        if s1 == true && s2 == true {
    	count ++
    	return true
        } else {
    	return false
        }
    }
    
    func countUnivalSubtrees(root *TreeNode) int {
        count = 0
        postOrder(root)
        return count
    }

---

-   Solution: post-order with only null as corner cases

    // Blog link: https://code.dennyzhang.com/count-univalue-subtrees
    // Basic Ideas: post-order
    // Complexity: Time O(n), Space O(1)
    /**
     * Definition for a binary tree node.
     * type TreeNode struct {
     *     Val int
     *     Left *TreeNode
     *     Right *TreeNode
     * }
     */
    var count int
    func postOrder(root *TreeNode) bool {
        if root == nil { return true }
        s1, s2 := postOrder(root.Left), postOrder(root.Right)
        if s1 == true && s2 == true {
    	if (root.Left != nil && root.Left.Val != root.Val) { return false }
    	if (root.Right != nil && root.Right.Val != root.Val) { return false }
    	count++
    	return true
        }
        return false
    }
    
    func countUnivalSubtrees(root *TreeNode) int {
        count = 0
        postOrder(root)
        return count
    }

