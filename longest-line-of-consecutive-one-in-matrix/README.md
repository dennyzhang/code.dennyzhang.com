# Leetcode: Longest Line of Consecutive One in Matrix     :BLOG:Medium:


---

Longest Line of Consecutive One in Matrix  

---

Similar Problems:  
-   [Unique Paths](https://brain.dennyzhang.com/unique-paths)
-   [Review: Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming), [Tag: #dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)

---

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.  
Example:  

    Input:
    [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,1]]
    Output: 3

Hint: The number of elements in the given matrix will not exceed 10,000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-line-of-consecutive-one-in-matrix)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/longest-line-of-consecutive-one-in-matrix
    ## Basic Ideas:
    ##
    ##   dp(i, j): 
    ##        horizontal:    dp(i, j-1)
    ##        vertical:      dp(i-1, j)
    ##        diagonal:      dp(i-1, j-1)
    ##        anti-diagonal: dp(i-1, j+1)
    ##
    ## Complexity: Time O(m*n), Space O(m*n)
    class Solution:
        def longestLine(self, M):
            """
            :type M: List[List[int]]
            :rtype: int
            """
            row_count = len(M)
            if row_count == 0: return 0
            col_count = len(M[0])
    
            dp = [[[0, 0, 0, 0] for j in range(col_count)] for i in range(row_count)]
            max_count = 0
            # dynamic programming
            for i in range(row_count):
                for j in range(col_count):
                    if M[i][j] == 0: continue
                    dp[i][j] = [1, 1, 1, 1]
                    if j>0: dp[i][j][0] = dp[i][j-1][0] + 1
                    if i>0: dp[i][j][1] = dp[i-1][j][1] + 1
                    if i>0 and j>0: dp[i][j][2] = dp[i-1][j-1][2] + 1
                    if i>0 and j<col_count-1: dp[i][j][3] = dp[i-1][j+1][3] + 1
                    max_count = max(max_count, max(dp[i][j]))
            return max_count