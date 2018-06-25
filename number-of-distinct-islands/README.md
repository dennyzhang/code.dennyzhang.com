
# Leetcode: Number of Distinct Islands     :BLOG:Medium:

---

Number of Distinct Islands  

---

Similar Problems:  

-   [Number of Distinct Islands II](https://code.dennyzhang.com/number-of-distinct-islands-ii)
-   Tag: [#island](https://code.dennyzhang.com/tag/island), [#dfs](https://code.dennyzhang.com/tag/dfs)

---

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.  

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.  

Example 1:  

    11000
    11000
    00011
    00011
    Given the above grid map, return 1.

Example 2:  

    11011
    10000
    00001
    11011
    Given the above grid map, return 3.

Notice that:  

    11
    1

and  

     1
    11

are considered different island shapes, because we do not consider reflection / rotation.  
Note: The length of each dimension in the given grid does not exceed 50.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-distinct-islands)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-distinct-islands/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/number-of-distinct-islands
    // Basic Ideas: dfs + hashmap
    // Note: In golang, we can't use tuple or slices as key for hashmap
    // Complexity: Time O(n*m), Space O(n*m*k)
    //             k=num_of_distinct_island
    import "strconv"
    var start_x, start_y int
    func dfs(grid [][]int, i int, j int, island string) string {
        if i<0 || i>=len(grid) || j<0 || j>=len(grid[0]) { return island }
        if grid[i][j] != 1 { return island }
        island += strconv.Itoa((i-start_x)*len(grid) + j-start_y)
        grid[i][j] = 2
        island = dfs(grid, i+1, j, island)
        island = dfs(grid, i-1, j, island)
        island = dfs(grid, i, j+1, island)
        island = dfs(grid, i, j-1, island)
        return island
    }
    
    func numDistinctIslands(grid [][]int) int {
        row_count := len(grid)
        if row_count == 0 { return 0 }
        hashmap := map[string]bool{}
        for i, row := range grid {
    	for j, _:= range row {
    	    start_x, start_y = i, j
    	    if row[j] == 1 {
    		island := dfs(grid, i, j, "")
    		hashmap[island] = true
    	    }
    	}
        }
        return len(hashmap)
    }

