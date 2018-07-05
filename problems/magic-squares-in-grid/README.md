# Leetcode: Magic Squares In Grid     :BLOG:Basic:


---

Magic Squares In Grid  

---

Similar Problems:  
-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.  

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).  

Example 1:  

    Input: [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    Output: 1
    Explanation: 
    The following subgrid is a 3 x 3 magic square:
    438
    951
    276
    
    while this one is not:
    384
    519
    762
    
    In total, there is only one magic square inside the given grid.

Note:  

    - 1 <= grid.length <= 10
    - 1 <= grid[0].length <= 10
    - 0 <= grid[i][j] <= 15

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/magic-squares-in-grid)  

Credits To: [leetcode.com](https://leetcode.com/problems/magic-squares-in-grid/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/magic-squares-in-grid
    // Basic Ideas: One pass + hashmap
    //
    // The center point must be 5. The sum of each list must be 15.
    //
    // [[1,8,6]
    //  [10,5,0]
    //  [4,2,9]]
    //
    // Complexity: Time O(n*m), Space O(1)
    func numMagicSquaresInside(grid [][]int) int {
        if len(grid) < 3 { return 0 }
        res := 0
        for i:=1; i<len(grid)-1; i++ {
            for j:=1; j<len(grid[0])-1; j++ {
                if grid[i][j] == 5 {
                    is_ok := true
                    m := make([]bool, 9)
                    m[4] = true
    
                    for _, offset := range [][]int{[]int{-1, -1}, []int{-1, 0}, 
                                                   []int{-1, 1}, []int{0, -1}} {
                        v1,v2 := grid[i+offset[0]][j+offset[1]], grid[i-offset[0]][j-offset[1]]
                        if v1<1 || v1>9 || v2<1 || v2>9 || 
                            v1+v2 != 10 || m[v1-1] == true || m[v2-1] == true { 
                            is_ok = false
                            break 
                        }
                        m[v1-1], m[v2-1] = true, true
                    }
                    if is_ok == true { res++ }
                }
            }
        }
        return res
    }