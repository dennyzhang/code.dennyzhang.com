# Leetcode: Transform to Chessboard     :BLOG:Hard:


---

Transform to Chessboard  

---

Similar Problems:  
-   Tag: [#math](https://code.dennyzhang.com/tag/math), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#game](https://code.dennyzhang.com/tag/game)

---

An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.  

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.  

Examples:  

    Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    Output: 2
    Explanation:
    One potential sequence of moves is shown below, from left to right:
    
    0110     1010     1010
    0110 --> 1010 --> 0101
    1001     0101     1010
    1001     0101     0101
    
    The first move swaps the first and second column.
    The second move swaps the second and third row.

    Input: board = [[0, 1], [1, 0]]
    Output: 0
    Explanation:
    Also note that the board with 0 in the top left corner,
    01
    10
    
    is also a valid chessboard.

    Input: board = [[1, 0], [1, 0]]
    Output: -1
    Explanation:
    No matter what sequence of moves you make, you cannot end with a valid chessboard.

Note:  

-   board will have the same number of rows and columns, a number in the range [2, 30].
-   board[i][j] will be only 0s or 1s.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/transform-to-chessboard)  

Credits To: [leetcode.com](https://leetcode.com/problems/transform-to-chessboard/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: XXX

    General Thinking:

    // Blog link: https://code.dennyzhang.com/transform-to-chessboard