# Leetcode: Print Binary Tree     :BLOG:Medium:


---

Print Binary Tree  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Print a binary tree in an m\*n 2D string array following these rules:  

The row number m should be equal to the height of the given binary tree.  
The column number n should always be an odd number.  
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.  
Each unused space should contain an empty string "".  
Print the subtrees following the same rules.  

    Example 1:
    Input:
         1
        /
       2
    Output:
    [["", "1", ""],
     ["2", "", ""]]

    Example 2:
    Input:
         1
        / \
       2   3
        \
         4
    Output:
    [["", "", "", "1", "", "", ""],
     ["", "2", "", "", "", "3", ""],
     ["", "", "4", "", "", "", ""]]

    Example 3:
    Input:
          1
         / \
        2   5
       / 
      3 
     / 
    4 
    Output:
    
    [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
     ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
     ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
     ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

Note: The height of binary tree is in the range of [1, 10].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/print-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/print-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/print-binary-tree
    // Basic Ideas: BFS
    // Fristly get the tree height: h
    // From level i to level i+1, we move the index by the offset of 2^(h-i-1)
    //      i starts with 1
    // Complexity:
    /**
     * Definition for a binary tree node.
     * type TreeNode struct {
     *     Val int
     *     Left *TreeNode
     *     Right *TreeNode
     * }
     */
    import (
            "strconv"
            "math"
    )
    
    type Node struct {
      index int
      treenode *TreeNode
    }
    
    func heightTree(root *TreeNode) int {
        if root == nil { return 0 }
        if root.Left ==  nil && root.Right == nil { return 1 }
        h := heightTree(root.Left)
        height_r := heightTree(root.Right)
        if height_r>h { h = height_r }
        return h+1    
    }
    
    func printTree(root *TreeNode) [][]string {
        res := [][]string{}
        height := heightTree(root)
        length := int(math.Pow(2, float64(height)))-1
        index := int(math.Pow(2, float64(height-1)))-1
        // BFS
        queue := []Node{Node{index, root}}
        for h:= 1; h<=height; h++ {
            items := make([]string, length)
            for i:= 0; i<length; i++ { items[i] = "" }
            offset := int(math.Pow(2, float64(height-h-1)))
            // caculate current row
            nodes := []Node{}
            for _, node := range queue{
                items[node.index] = strconv.Itoa(node.treenode.Val)
                if node.treenode.Left != nil {
                    nodes = append(nodes, Node{node.index-offset, node.treenode.Left})
                }
                if node.treenode.Right != nil {
                    nodes = append(nodes, Node{node.index+offset, node.treenode.Right})
                }
            }
            queue = []Node{}
            for _, node := range nodes { queue = append(queue, node) }
            // collect current row
            res = append(res, items)
        }
        return res
    }