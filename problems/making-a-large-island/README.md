
# Leetcode: Making A Large Island     :BLOG:Hard:

---

Making A Large Island  

---

Similar Problems:  

-   [Number of Distinct Islands II](https://code.dennyzhang.com/number-of-distinct-islands-ii)
-   Tag: [#island](https://code.dennyzhang.com/tag/island), [#dfs](https://code.dennyzhang.com/tag/dfs)

---

In a 2D grid of 0s and 1s, we change at most one 0 to a 1.  

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).  

Example 1:  

    Input: [[1, 0], [0, 1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:  

    Input: [[1, 1], [1, 0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 1.

Example 3:  

    Input: [[1, 1], [1, 1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 1.

Notes:  

    - 1 <= grid.length = grid[0].length <= 50.
    - 0 <= grid[i][j] <= 1.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/making-a-large-island)  

Credits To: [leetcode.com](https://leetcode.com/problems/making-a-large-island/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/making-a-large-island
    // Basic Ideas: dfs + hashmap
    //
    //   We track all 0s which is the islands' boundry
    //   map2: island_size: size of each island
    //   Then we loop map1, if we change that item what islands we can connect together.
    //
    // Complexity: Time O(n*m), Space O(n*m)
    import (
    	"fmt"
    	"strings"
    	"strconv"
    )
    var island_id int
    var island_size map[int]int
    var boundry map[string]bool
    
    func dfs(grid [][]int, i int, j int) {
        // get island size, and neighbor 0s
        if i<0 || i>=len(grid) || j<0 || j>=len(grid[0]) { return }
        if grid[i][j] == 0 {
    	point := fmt.Sprintf("%d-%d", i, j)
    	boundry[point] = true
        }
        if grid[i][j] != 1 { return }
        grid[i][j] = island_id
        island_size[island_id]++
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
    }
    
    func largestIsland(grid [][]int) int {
        if len(grid) == 0 { return 0 }
    
        island_size = make(map[int]int)
        boundry = make(map[string]bool)
        island_id = 2
        for i, row := range grid {
    	for j, v := range row {
    	    if v == 1 {
    		dfs(grid, i, j)
    		island_id++
    	    }
    	}
        }
        res := 0
        for v := range island_size {
    	if island_size[v]>res { res = island_size[v] }
        }
        // check boundry
        for point := range boundry {
    	l := strings.Split(point, "-")
    	i, _:= strconv.Atoi(l[0])
    	j, _:= strconv.Atoi(l[1])
    	count := 1
    	m := make(map[int]bool)
    	for _, k := range [][]int{[]int{0, 1}, []int{0, -1}, []int{1, 0}, []int{-1, 0}} {
    	    i2, j2 := i+k[0], j+k[1]
    	    if i2<0 || i2>=len(grid) || j2<0 || j2>=len(grid[0]) { continue }
    	    v := grid[i2][j2]
    	    if v != 0 && m[v] == false {
    		count += island_size[v]
    		m[v] = true
    	    }
    	}
    	if count > res { res = count }
        }
        // mark markself, if no island is found
        if res == 0 { res = 1 }
        return res
    }

