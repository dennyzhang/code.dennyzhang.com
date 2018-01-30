# Leetcode: Unique Paths II     :BLOG:Medium:


---

Unique Paths II  

---

Similar Problems:  
-   [Leetcode: Unique Paths](https://brain.dennyzhang.com/unique-paths)
-   Tag: [#dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)

---

Follow up for "Unique Paths":  

Now consider if some obstacles are added to the grids. How many unique paths would there be?  

An obstacle and empty space is marked as 1 and 0 respectively in the grid.  

For example,  
There is one obstacle in the middle of a 3x3 grid as illustrated below.  

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]

The total number of unique paths is 2.  

Note: m and n will be at most 100.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/unique-paths-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/unique-paths-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/unique-paths-ii
    ## Basic Ideas: dynamic programming
    ##  Very similar to https://brain.dennyzhang.com/unique-paths
    ##
    ##              f(i, j) = if it's obstacle, 0
    ##                        else: f(i-1, j) + f(i, j-1)
    ##
    ## Complexity: Time O(m*n), Space O(m*n)
    class Solution(object):
        def uniquePathsWithObstacles(self, obstacleGrid):
            """
            :type obstacleGrid: List[List[int]]
            :rtype: int
            """
            row_count = len(obstacleGrid)
            if row_count == 0: return 0
            col_count = len(obstacleGrid[0])
            # use default values to simplify the code
            matrix = [[0 for x in xrange(col_count)] for y in xrange(row_count)]
    
            matrix[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
            # first row
            i = 0
            for j in range(1, col_count):
                if obstacleGrid[i][j] == 0: matrix[i][j] = matrix[i][j-1]
    
            # first column
            j = 0
            for i in range(1, row_count):
                if obstacleGrid[i][j] == 0: matrix[i][j] = matrix[i-1][j]
    
            # others
            for i in range(1, row_count):
                for j in range(1, col_count):
                    if obstacleGrid[i][j] == 0:
                        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    
            return matrix[-1][-1]