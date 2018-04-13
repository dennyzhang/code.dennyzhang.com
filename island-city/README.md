# LintCode: Island City     :BLOG:Basic:


---

Island City  

---

Similar Problems:  
-   [Number of Islands](https://code.dennyzhang.com/number-of-islands)
-   [Review: Graph Problems](https://code.dennyzhang.com/review-graph)
-   Tag: [#graph](https://code.dennyzhang.com/tag/graph), [#dfs](https://code.dennyzhang.com/tag/dfs), [#bfs](https://code.dennyzhang.com/tag/bfs)

---

Given a matrix of size n x m, the elements in the matrix are 0,1,2.  

0 for the sea, 1 for the island, and 2 for the city on the island(You can assume that 2 is built on 1, ie 2 also represents the island).  
If two 1 are adjacent, then these two 1 belong to the same island. Find the number of islands with at least one city.  

Notice  
1.  We only consider up, down, left and right as adjacent.
2.  n <= 100, m <= 100.
3.  You can assume that the four sides of the matrix are surrounded by the sea.

Example  

    Given mat =
    [
         [1,1,0,0,0],
         [0,1,0,0,1],
         [0,0,0,1,1],
         [0,0,0,0,0],
         [0,0,0,0,1]
    ]

, return 0.  

    Explanation:
    There are 3 islands, but none of them contain cities.

    Given mat =
    [
         [1,1,0,0,0],
         [0,1,0,0,1],
         [0,0,2,1,2],
         [0,0,0,0,0],
         [0,0,0,0,2]
    ]

, return 2.  

    Explanation:
    There are 3 islands, and two of them have cities.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/island-city)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/island-city/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/island-city
    class Solution:
        """
        @param grid: an integer matrix
        @return: an integer 
        """
        def numIslandCities(self, grid):
            ## Basic Ideas: dfs
            ## Complexity: Time O(m*n), Space O(1)
            row_count = len(grid)
            if row_count == 0: return 0
            col_count = len(grid[0])
            self.count = 0
            for i in range(row_count):
                for j in range(col_count):
                    if grid[i][j] in [1, 2]:
                        self.first_found = True
                        self.dfs(grid, i, j, row_count, col_count)
            return self.count
    
        def dfs(self, grid, i, j, row_count, col_count):
            if i<0 or i>=row_count or \
                j<0 or j>=col_count:
                    return
    
            if grid[i][j] not in [1, 2]: return
    
            if grid[i][j] == 2 and self.first_found:
                self.count += 1
                self.first_found = False
    
            grid[i][j] = -1
            self.dfs(grid, i, j+1, row_count, col_count)
            self.dfs(grid, i, j-1, row_count, col_count)
            self.dfs(grid, i-1, j, row_count, col_count)
            self.dfs(grid, i+1, j, row_count, col_count)