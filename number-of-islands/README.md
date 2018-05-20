# Leetcode: Number of Islands     :BLOG:Basic:


---

Number of Islands  

---

Similar Problems:  
-   [Island City](https://code.dennyzhang.com/island-city)
-   [Review: Graph Problems](https://code.dennyzhang.com/review-graph)
-   [Review: BFS Problems](https://code.dennyzhang.com/review-bfs)
-   Tag: [#graph](https://code.dennyzhang.com/tag/graph), [#dfs](https://code.dennyzhang.com/tag/dfs), [#bfs](https://code.dennyzhang.com/tag/bfs)

---

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.  

    Example 1:
    
    11110
    11010
    11000
    00000
    Answer: 1

    Example 2:
    
    11000
    11000
    00100
    00011
    Answer: 3

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-islands)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-islands/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/number-of-islands
    class Solution(object):
        ## Basic Ideas: Avoid duplicate counting.
        ##   Mark all adjacent 1 to X. Thus we can avoid counting one the same island multiple times.
        ##
        ## Complexity: Time O(m*n), Space O(1)
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            self.row_count = len(grid)
            if self.row_count == 0: return 0
            self.col_count = len(grid[0])
    
            res = 0
            for i in xrange(self.row_count):
                for j in xrange(self.col_count):
                    if grid[i][j] == '1':
                        res += 1
                        self.DFSMark(grid, i, j)
            return res
    
        def DFSMark(self, grid, i, j):
            if i < 0 or i >= self.row_count \
                or j < 0 or j >= self.col_count:
                return
    
            # stop digging, if not '1'
            if grid[i][j] != '1': return
    
            grid[i][j] = 'X'
            # mark four positions in a recursive way
            self.DFSMark(grid, i-1, j)
            self.DFSMark(grid, i+1, j)
            self.DFSMark(grid, i, j-1)
            self.DFSMark(grid, i, j+1)