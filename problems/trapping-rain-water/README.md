# Leetcode: Trapping Rain Water     :BLOG:Hard:


---

Trapping Rain Water  

---

Similar Problems:  
-   [Product of Array Except Self](https://code.dennyzhang.com/product-of-array-except-self)
-   [Trapping Rain Water](https://code.dennyzhang.com/container-water)
-   Tag: [#trappingrain](https://code.dennyzhang.com/tag/trappingrain), [#twopass](https://code.dennyzhang.com/tag/twopass)

---

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.  
![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/rainwater_trap.png)  
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!  

Example:  

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/trapping-rain-water)  

Credits To: [leetcode.com](https://leetcode.com/problems/trapping-rain-water/description/)  

Leave me comments, if you have better ways to solve.  

---

Similar problem: [Product of Array Except Self](https://code.dennyzhang.com/product-of-array-except-self)  

-   Solution: Two pass

    // Blog link: https://code.dennyzhang.com/trapping-rain-water
    // Basic Ideas: Two Pass
    // For each cell, find the left maximum and right maximum
    // Then caculate how much water current cell can hold
    //
    // Sapmle Data:
    //    0,1,0,2,1,0,1,3,2,1,2,1
    //    3,3,3,3,3,3,3,3,2,2,2,1
    //    0,1,1,2,2,2,2,3,3,3,3,3
    // Complexity: Time O(n), Space O(n)
    func trap(height []int) int {
        lmax_list := make([]int, len(height))
        rmax_list := make([]int, len(height))
        max := 0
        // from left to right
        for i:=0; i<len(height); i++ {
            if height[i] > max { max = height[i] }
            lmax_list[i] = max
        }
        // from right to left
        max = 0
        for i:= len(height)-1; i>=0; i-- {
            if height[i] > max { max = height[i] }
            rmax_list[i] = max
        }
        // collect result
        res, border := 0, 0
        for i:=1; i<len(height)-1; i++ {
            border = lmax_list[i]
            if rmax_list[i] < border { border = rmax_list[i] }
            if height[i] < border { res += border-height[i] }
        }
        return res
    }