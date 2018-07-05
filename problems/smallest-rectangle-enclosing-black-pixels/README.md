# Leetcode: Smallest Rectangle Enclosing Black Pixels     :BLOG:Medium:


---

Smallest Rectangle Enclosing Black Pixels  

---

Similar Problems:  
-   [Number of Distinct Islands](https://code.dennyzhang.com/number-of-distinct-islands)
-   Tag: [#island](https://code.dennyzhang.com/tag/island), [#dfs](https://code.dennyzhang.com/tag/dfs)

---

An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.  

Example:  

    Input:
    [
      "0010",
      "0110",
      "0100"
    ]
    and x = 0, y = 2
    
    Output: 6

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/smallest-rectangle-enclosing-black-pixels)  

Credits To: [leetcode.com](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: dfs island issues

Similar Problems:  
-   [Number of Distinct Islands](https://code.dennyzhang.com/number-of-distinct-islands)
-   Tag: [#island](https://code.dennyzhang.com/tag/island), [#dfs](https://code.dennyzhang.com/tag/dfs)

    // Blog link: https://code.dennyzhang.com/smallest-rectangle-enclosing-black-pixels
    // Basic Ideas: dfs
    //  region: (max_x-min_x+1)*(max_y-min_y+1)
    // Complexity: Time O(n*m), Space O(1)
    
    var min_x, max_x, min_y, max_y int
    func dfs(image [][]byte, x int, y int) {
        if x<0 || x>=len(image) || y<0 || y>=len(image[0]) { return }
        if image[x][y] != '1' { return }
        image[x][y] = '2'
        if x<min_x { min_x = x }
        if x>max_x { max_x = x }
        if y<min_y { min_y = y }
        if y>max_y { max_y = y }
        dfs(image, x+1, y)
        dfs(image, x-1, y)
        dfs(image, x, y+1)
        dfs(image, x, y-1)
    }
    func minArea(image [][]byte, x int, y int) int {
        if len(image) == 0 { return 0 }
        min_x, max_x = x, x
        min_y, max_y = y, y
        dfs(image, x, y)
        return (max_x-min_x+1)*(max_y-min_y+1)
    }