# Leetcode: Max Increase to Keep City Skyline     :BLOG:Medium:


---

Max Increase to Keep City Skyline  

---

Similar Problems:  
-   [Lonely Pixel I](https://brain.dennyzhang.com/lonely-pixel-i)
-   Tag: [#array](https://brain.dennyzhang.com/tag/array)

---

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.  

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.  

What is the maximum total sum that the height of the buildings can be increased?  

Example:  

    Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    Output: 35
    Explanation: 
    The grid is:
    [ [3, 0, 8, 4], 
      [2, 4, 5, 7],
      [9, 2, 6, 3],
      [0, 3, 1, 0] ]
    
    The skyline viewed from top or bottom is: [9, 4, 8, 7]
    The skyline viewed from left or right is: [8, 7, 9, 3]
    
    The grid after increasing the height of buildings without affecting skylines is:
    
    gridNew = [ [8, 4, 8, 7],
                [7, 4, 7, 7],
                [9, 4, 8, 7],
                [3, 3, 3, 3] ]

Notes:  

-   1 < grid.length = grid.length <= 50.
-   All heights grid[i][j] are in the range [0, 100].
-   All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/max-increase-to-keep-city-skyline)  

Credits To: [leetcode.com](https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/max-increase-to-keep-city-skyline
    ## Basic Ideas:
    ## Complexity: O(m*n), Space O(n+m)
    class Solution:
        def maxIncreaseKeepingSkyline(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            row_count = len(grid)
            col_count = len(grid[0])
            hl = [-1 for i in range(col_count)]
            vl = [-1 for i in range(row_count)]
            for i in range(row_count):
                for j in range(col_count):
                    hl[j] = max(hl[j], grid[i][j])
                    vl[i] = max(vl[i], grid[i][j])
            res = 0
            for i in range(row_count):
                for j in range(col_count):
                    candidate = min(hl[j], vl[i])
                    if grid[i][j] < candidate:
                        res += candidate - grid[i][j]
            return res

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum" href="#fnr.1">1</a></sup> <p>DEFINITION NOT FOUND.</p></div>


</div>
</div>