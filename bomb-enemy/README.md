# Leetcode: Bomb Enemy     :BLOG:Medium:


---

Bomb Enemy  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming), [Tag: #dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)

---

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.  
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.  
Note that you can only put the bomb at an empty cell.  

Example:  

    For the given grid
    
    0 E 0 0
    E 0 W E
    0 E 0 0
    
    return 3. (Placing a bomb at (1,1) kills 3 enemies)

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/bomb-enemy)  

Credits To: [leetcode.com](https://leetcode.com/problems/bomb-enemy/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/bomb-enemy
    ## Basic Ideas: dynamic programming
    ##
    ## dp[i] = (max_enemies_x, max_enemies_y)
    ##          max_enemies_x: from top to current row
    ##          max_enemies_y: from left to current column
    ##
    ##  f([i][j][0]) = g([i][j-1][0], grid[i][j])
    ##  f([i][j][1]) = g([i-1][j][1], grid[i][j])
    ##
    ## Assumption: if we place a boom in 'W', we will kill no enemies
    ##
    ## Complexity: Time O(n*n), Space O(n)
    class Solution:
        def maxKilledEnemies(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            row_count = len(grid)
            if row_count == 0: return 0
            col_count = len(grid[0])
    
            dp = [(0, 0) for i in range(col_count)]
    
            # initial starting point
            ch = grid[0][0]
            max_count = 0
            if ch == 'W':
                dp[0] = (0, 0)
            elif ch == 'E':
                dp[0] = (1, 1)
                max_count = 1
            else:
                dp[0] = (0, 0)
    
            # calculate all values
            for i in range(row_count):
                for j in range(col_count):
                    if i == 0 and j == 0: continue
                    ch = grid[i][j]
                    if ch == 'W':
                        dp[j] = (0, 0) 
                    elif ch == 'E':
                        if i == 0:
                            dp[j] = (1, dp[j-1][1]+1)
                        else:
                            dp[j] = (dp[j][0]+1, dp[j-1][1]+1)
                        max_count = max(max_count, max(dp[j])-1)
                    else:
                        dp[j] = (dp[j][0], dp[j-1][1])
                        max_count = max(max_count, max(dp[j]))
            return max_count