# Leetcode: Dungeon Game     :BLOG:Hard:


---

Dungeon Game  

---

Similar Problems:  
-   [Unique Paths](https://code.dennyzhang.com/unique-paths)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#game](https://code.dennyzhang.com/tag/game), [#classic](https://code.dennyzhang.com/tag/classic), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.  

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.  

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).  

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.  

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.  

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.  

    -2 (K)  -3      3
    -5      -10     1
    10      30      -5 (P)

Note:  

-   The knight's health has no upper bound.
-   Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/dungeon-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/dungeon-game/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: Dynamic programming

**Key Observations:**  

    // We don't know the miminum health we need from top-left to bottom-right
    // But we do know the miimum health we need from bottom-right to top-left

    // Blog link: https://code.dennyzhang.com/dungeon-game
    // Basic Ideas: Dynamic programming
    //
    // We don't know the miminum health we need from top-left to bottom-right
    // But we do know the miimum health we need from bottom-right to top-left
    //
    // dp[i][j]: mininum health we need for current cell.
    // dp[i][j] = 
    //          next_dp = min(dp[i+1][j], dp[i][j+1])
    //          dungeon[i][j] >= next_dp? 1 : next_dp-dungeon[i][j]
    // Complexity: Time O(n*m), Space O(m)
    func calculateMinimumHP(dungeon [][]int) int {
        row_count := len(dungeon)
        if row_count == 0 { return 0 }
        col_count := len(dungeon[0])
        // Initial status
        dp := make([]int, col_count+1)
        for i, _ := range dp { dp[i] = 1<<31 - 1 }
        dp[col_count-1] = 1
        // We explore from bottom-right to top-left
        for i := row_count-1; i>=0; i-- {
            for j:= col_count-1; j>=0; j-- {
                next_dp := dp[j]
                if next_dp > dp[j+1] { next_dp = dp[j+1] }
                if dungeon[i][j] >= next_dp {
                    dp[j] = 1
                } else {
                    dp[j]= next_dp - dungeon[i][j]
                }
            }
        }
        return dp[0]
    }