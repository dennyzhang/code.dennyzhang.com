# Leetcode: Number of Boomerangs     :BLOG:Medium:


---

Number of Boomerangs  

---

Similar Problems:  
-   [Line Reflection](https://code.dennyzhang.com/line-reflection)
-   Tag: [#math](https://code.dennyzhang.com/tag/math), [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).  

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).  

    Example:
    Input:
    [[0,0],[1,0],[2,0]]
    
    Output:
    2
    
    Explanation:
    The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-boomerangs)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-boomerangs/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: hashmap with hashmap as value

    // Blog link: https://code.dennyzhang.com/number-of-boomerangs
    // Basic Ideas: hashmap
    //
    // m[0] = [1:[1], 4:[2]]
    // m[1] = [1:[0, 2]]
    // m[2] = [1:[1], 4:[0]]
    //
    // Complexity: Time O(n*n), Space O(n*n)
    func numberOfBoomerangs(points [][]int) int {
      res := 0
      n := len(points)
      array := make([]map[int]int, n)
      for i:= 0; i<n; i++ { array[i] = map[int]int{} }
      for i, point1 := range points {
        m := array[i]
        for j, point2 := range points {
          if i == j { continue }
          v1, v2 := point1[0]-point2[0], point1[1]-point2[1]
          m[v1*v1+v2*v2] += 1
        }
      }
      // collect results
      for _, m := range array {
        for d := range m {
          if m[d]>1 {
            res += m[d]*(m[d]-1)
          }
        }
      }
      return res
    }

-   Solution: hashmap with int as value

    // Blog link: https://code.dennyzhang.com/number-of-boomerangs
    // Basic Ideas: hashmap
    //    hashmap with value as int
    // m = [1:1, 4:1]
    // m = [1:2]
    // m = [1:1, 4:1]
    //
    // Complexity: Time O(n*n), Space O(n)
    
    func numberOfBoomerangs(points [][]int) int {
      res := 0
      for i, point1 := range points {
        m := map[int]int{}
        for j, point2 := range points {
          if i == j { continue }
          v1, v2 := point1[0]-point2[0], point1[1]-point2[1]
          m[v1*v1+v2*v2] += 1
        }
        // collect results
        for d:= range m {
            if m[d]>1 { res += m[d]*(m[d]-1)}
        }
      }
      return res
    }