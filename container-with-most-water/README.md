# Leetcode: Container With Most Water     :BLOG:Medium:


---

Get the most water from containers  

---

Similar Problems:  
-   Tag: [#trappingrain](https://code.dennyzhang.com/tag/trappingrain), [#twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Given n non-negative integers a1, a2, &#x2026;, an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.  

Note: You may not slant the container and n is at least 2.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/container-with-most-water)  

Credits To: [leetcode.com](https://leetcode.com/problems/container-with-most-water/description/)  

Leave me comments, if you have better ways to solve.  

---

**Key Observations:**  

    By moving shorter end pointer further doesn't eliminate the final answer

-   Solution: Two Pointer

    // Blog link: https://code.dennyzhang.com/container-with-most-water
    // Basic Ideas: Two pointer
    //   Start with l, r = 0, len(l)-1
    //   Then move the pointer of shorter value
    //     Let's check the case that both pointers are the same the value.
    //     We won't find a better solution with only one edge of left pointer or right pointer.
    //     Thus we can move either pointer
    // Complexity: Time O(n), Space O(1)
    func maxArea(height []int) int {
        l, r := 0, len(height)-1
        res, v := 0, 0
        for l<r {
            if height[l] <= height[r] {
                v = height[l]*(r-l)
                l++
            } else {
                v = height[r]*(r-l)
                r--
            }
            if v>res { res = v }
        }
        return res
    }

-   Solution: Two Pointer + Pruning

    // Blog link: https://code.dennyzhang.com/container-with-most-water
    // Basic Ideas: Two pointer
    //   Start with l, r = 0, len(l)-1
    //   Then move the pointer of shorter value
    //     Let's check the case that both pointers are the same the value.
    //     We won't find a better solution with only one edge of left pointer or right pointer.
    //     Thus we can move either pointer
    // Complexity: Time O(n), Space O(1)
    func maxArea(height []int) int {
        l, r := 0, len(height)-1
        res, v := 0, 0
        for l<r {
            lmax, rmax := height[l], height[r]
            if height[l] <= height[r] {
                v = height[l]*(r-l)
            } else {
                v = height[r]*(r-l)
            }
            if v>res { res = v }
            if height[l] <= height[r] {
                for l<r && height[l]<=lmax { l++ }
            } else {
                for l<r && height[r]<=rmax { r-- }
            }
        }
        return res
    }