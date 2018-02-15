# Leetcode: Binary Tree Vertical Order Traversal     :BLOG:Medium:


---

Binary Tree Vertical Order Traversal  

---

Similar Problems:  

-   Tag: [#binarytree](https://brain.dennyzhang.com/tag/binarytree)

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