# Leetcode: Valid Square     :BLOG:Amusing:


---

Given the coordinates of four points in 2D space, return whether the four points could construct a square.  

---

Similar Problems:  
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   Tag: [math](https://code.dennyzhang.com/tag/math)

---

Given the coordinates of four points in 2D space, return whether the four points could construct a square.  

The coordinate (x,y) of a point is represented by an integer array with two integers.  

    Example:
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True

Note:  

1.  All the input integers are in the range [-10000, 10000].
2.  A valid square has four equal sides with positive length and four equal angles (90-degree angles).
3.  Input points have no order.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-square)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-square/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/valid-square
    // Basic Ideas: math
    // Get all the distances. There should be only 2 types: a, b
    // We shall find 4 a, 2 b. And a*a+a*a=b*b
    //
    // Complexity: Time O(1), Space O(1)
    func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
        points := [][]int{p1, p2, p3, p4}
        distances := map[int]int{}
        long_edge := 0
        for i, p := range points {
            for j:=i+1; j<=3; j++ {
                q := points[j]
                d := (p[0]-q[0])*(p[0]-q[0]) + (p[1]-q[1])*(p[1]-q[1])
                distances[d] += 1
                if d>long_edge { long_edge = d }
            }
        }
        if len(distances) != 2 || distances[long_edge] !=2 { return false }
        for v := range distances {
            if v==long_edge { continue }
            if distances[v]!=4 || v*2 != long_edge { return false }
        }
        return true
    }