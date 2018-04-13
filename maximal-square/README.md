# Leetcode: Maximal Square     :BLOG:Medium:


---

Maximal Square  

---

Similar Problems:  
-   [Unique Paths](https://code.dennyzhang.com/unique-paths)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.  

For example, given the following matrix:  

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

Return 4.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximal-square)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximal-square/description/)  

Leave me comments, if you have better ways to solve.  

<<<<<<< HEAD  

    // Blog link: https://code.dennyzhang.com/maximal-square
    // Basic Ideas: dynamic programming
    //   one pass
    //
    //  dp(i, j) depends on dp(i-1, j-1)
    //
    // Complexity: Time O(n*m), Space O(n*m)
    func maximalSquare(matrix [][]byte) int {
        row_count := len(matrix)
        if row_count == 0 {return 0}
        col_count := len(matrix[0])
        dp := make([][]int, row_count)
        res := 0
        for i := range dp { dp[i] = make([]int, col_count) }
        for i := range dp {
            for j := range dp[i] {
                // base case
                if i == 0 || j == 0 {
                    if string(matrix[i][j]) == "0" {
                        dp[i][j] = 0
                    } else {
                        dp[i][j] = 1
                        if dp[i][j] > res { res = dp[i][j] }
                    }
                    continue
                }
                // normal case
                if string(matrix[i][j]) != "0" {
                    if string(matrix[i-1][j]) == "1" && string(matrix[i][j-1]) == "1" {
                        // TODO
                        dp[i][j] = dp[i-1][j-1] + 3
                    } else {
                        dp[i][j] = 1
                    }
                }
                if dp[i][j] > res { res = dp[i][j] }
            }
        }
        return res
    }
    =======
    #+BEGIN_SRC python
    ## Blog link: https://code.dennyzhang.com/maximal-square
    
    >>>>>>> 123cc57c2e4abe14e48c40bfd5bdc5982e4e0c29