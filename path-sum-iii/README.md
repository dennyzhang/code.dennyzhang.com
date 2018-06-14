# Leetcode: Path Sum III     :BLOG:Amusing:


---

Path Sum III  

---

Similar Problems:  

-   [Review: Recursive Problems](https://code.dennyzhang.com/review-recursive)
-   Tag: [#recursive](https://code.dennyzhang.com/tag/recursive)

---

You are given a binary tree in which each node contains an integer value.  

Find the number of paths that sum to a given value.  

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).  

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.  

    Example:
    
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
    
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    
    Return 3. The paths that sum to 8 are:
    
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/path-sum-iii)  

Credits To: [leetcode.com](https://leetcode.com/problems/path-sum-iii/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/path-sum-iii
    // Basic Ideas: Recursive
    // Complexity: Time O(n^2), Space O(n)
    /**
     * Definition for a binary tree node.
     * type TreeNode struct {
     *     Val int
     *     Left *TreeNode
     *     Right *TreeNode
     * }
     */
    
    func pathSumFrom(root *TreeNode, sum int) int {
        if root == nil { return 0 }
        res := 0
        if root.Val == sum { res++ }
        res += pathSumFrom(root.Left, sum-root.Val)
        res += pathSumFrom(root.Right, sum-root.Val)
        return res
    }
    
    func pathSum(root *TreeNode, sum int) int {
        if root == nil { return 0 }
        return pathSumFrom(root, sum) + pathSum(root.Left, sum) + pathSum(root.Right, sum)
    }