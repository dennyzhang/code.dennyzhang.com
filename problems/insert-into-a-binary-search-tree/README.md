
# Leetcode: Insert into a Binary Search Tree     :BLOG:Basic:

---

Insert into a Binary Search Tree  

---

Similar Problems:  

-   Tag: [#binarytree](https://code.dennyzhang.com/tag/binarytree)

---

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.  

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.  

For example,  

Given the tree:  

            4
           / \
          2   7
         / \
        1   3
    
    And the value to insert: 5

You can return this binary search tree:  

         4
       /   \
      2     7
     / \   /
    1   3 5

This tree is also valid:  

         5
       /   \
      2     7
     / \   
    1   3
         \
          4

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/insert-into-a-binary-search-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/insert-into-a-binary-search-tree
    // Basic Ideas:
    //
    // Complexity:
    /**
     * Definition for a binary tree node.
     * type TreeNode struct {
     *     Val int
     *     Left *TreeNode
     *     Right *TreeNode
     * }
     */
    func insertIntoBST(root *TreeNode, val int) *TreeNode {
        p := root
        for true {
    	if p.Val > val {
    	    // left
    	    if p.Left == nil {
    		p.Left = &TreeNode{val, nil, nil}
    		break
    	    }
    	    p = p.Left
    	} else {
    	    if p.Right == nil {
    		p.Right = &TreeNode{val, nil, nil}
    		break
    	    }
    	    p = p.Right
    	}
        }
        return root
    }

