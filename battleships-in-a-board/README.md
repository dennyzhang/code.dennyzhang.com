# Leetcode: Battleships in a Board     :BLOG:Basic:


---

Battleships in a Board  

---

Similar Problems:  
-   [Tag: #array](https://code.dennyzhang.com/tag/array)

---

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:  
You receive a valid board, made of only battleships or empty slots.  
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.  
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.  

Example:  

    X..X
    ...X
    ...X
    In the above board there are 2 battleships.

Invalid Example:  

    ...X
    XXXX
    ...X
    This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:  
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/battleships-in-a-board)  

Credits To: [leetcode.com](https://leetcode.com/problems/battleships-in-a-board/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/battleships-in-a-board
    ## Basic Ideas
    ##   Check from left to right, top to down
    ##   If current digit is '1' and above digit is not '1', we keep moving left
    ## 
    ## Complexity: Time O(n*m), Space O(1)
    class Solution:
        def countBattleships(self, board):
            """
            :type board: List[List[str]]
            :rtype: int
            """
            row_count = len(board)
            if row_count == 0: return 0
            col_count = len(board[0])
            res = 0
            for i in range(row_count):
                for j in range(col_count):
                    if i!= 0 and board[i-1][j] == 'X': continue
                    if j!= 0 and board[i][j-1] == 'X': continue
                    if board[i][j] == 'X': res += 1
            return res