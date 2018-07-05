# Leetcode: Brick Wall     :BLOG:Medium:


---

Brick Wall  

---

Similar Problems:  
-   [Split Array into Consecutive Subsequences](https://code.dennyzhang.com/split-array-into-consecutive-subsequences)
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#hashmap](https://code.dennyzhang.com/tag/hashmap), [#limitedrange](https://code.dennyzhang.com/tag/limitedrange)

---

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.  

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.  

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.  

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.  

Example:  

    Input: 
    [[1,2,2,1],
     [3,1,2],
     [1,3,2],
     [2,4],
     [3,1,2],
     [1,3,1,1]]
    Output: 2
    Explanation:

![img](//raw.githubusercontent.com/DennyZhang/images/master/code/brick_wall.png)  

Note:  
1.  The width sum of bricks in different rows are the same and won't exceed INT\_MAX.
2.  The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/brick-wall)  

Credits To: [leetcode.com](https://leetcode.com/problems/brick-wall/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/brick-wall
    // Basic Ideas: hashmap
    //    Find all locations where we can draw a line by adding items
    //    For any given location, let's say the width from left to current is v
    //    The bricks it hits will be row_of_wall - v
    //
    // Complexity: Time O(n*m), Space O(1)
    //       There would be no more than 20,000 keys in hashmap
    func leastBricks(wall [][]int) int {
        count := 0
        m := make(map[int]int)
        for _, row := range wall {
            length := 0
            for i, width := range row {
                if i == len(row)-1 { continue }
                length += width
                m[length] += 1
                v, _ := m[length]
                if v > count { count = v}
            }
        }
        return len(wall)-count
    }