# Leetcode: Unique Paths     :BLOG:Basic:


---

Unique Paths  

---

Similar Problems:  
-   [Leetcode: Unique Paths II](https://code.dennyzhang.com/unique-paths-ii)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming), [Tag: #dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).  

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).  

How many possible unique paths are there?  

![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/robot_maze.png)  

Above is a 3 x 7 grid. How many possible unique paths are there?  

Note: m and n will be at most 100.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/unique-paths)  

Credits To: [leetcode.com](https://leetcode.com/problems/unique-paths/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/unique-paths
    class Solution(object):
        ## Basic Ideas: Dynamic programming
        ##              For the previous step of finish point, it should come from either up or left
        ##              f(i, j) = f(i-1, j) + f(j, j-1)
        ##
        ## Complexity: Time O(m*n), Space O(m)
        def uniquePaths(self, m, n):
            """
            :type m: int
            :type n: int
            :rtype: int
            """
            if m == 0 or n == 0: return 0
            dp = [1 for i in range(n)]
            for i in range(1, m):
                for j in range(1, n):
                    dp[j] = dp[j-1] + dp[j]
            return dp[-1]
    
        ## Basic Ideas: Dynamic programming
        ##              For the previous step of finish point, it should come from either up or left
        ##              f(i, j) = f(i-1, j) + f(j, j-1)
        ##
        ## Complexity: Time O(m*n), Space O(m*n)
        def uniquePaths_v1(self, m, n):
            """
            :type m: int
            :type n: int
            :rtype: int
            """
            if m == 0 or n == 0: return 0
            matrix = [None]*m
            for i in range(m): matrix[i] = [1]*n
            for i in range(1, m):
                for j in range(1, n):
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
            return matrix[-1][-1]