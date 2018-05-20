# Leetcode: Sort Transformed Array     :BLOG:Medium:


---

Sort Transformed Array  

---

Similar Problems:  
-   [Split Array With Same Average](https://code.dennyzhang.com/split-array-with-same-average)
-   Tag: [#math](https://code.dennyzhang.com/tag/math), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax\*x + bx + c to each element x in the array.  

The returned array must be in sorted order.  

Expected time complexity: O(n)  

Example:  

    nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
    
    Result: [3, 9, 15, 33]

    nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
    
    Result: [-23, -5, 1, 7]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sort-transformed-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/sort-transformed-array/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/sort-transformed-array
    // Basic Ideas: math. two-pointer
    // f(x) = a*x*x+b*x+c
    //   Let's say x1<x2<x3.
    //   If a>=0, f(x2) <= max(f(x1), f(x3))
    //   Else, f(x2) >= min(f(x1), f(x3))
    // So we can get the biggest value, either from the left or the right
    // Complexity: Time O(n), Space O(n)
    func sortTransformedArray(nums []int, a int, b int, c int) []int {
        nums2 := make([]int, len(nums))
        for i, x:= range nums { nums2[i] = a*x*x+b*x+c }
        index, offset := 0, 1
        // We know the maximum first
        if a>=0 { index, offset = len(nums)-1, -1 }
        res := make([]int, len(nums))
        l, r := 0, len(nums)-1
        for l<=r {
            if a>=0 {
                // We know the maximum first
                if nums2[l]>nums2[r] {
                    res[index] = nums2[l]
                    l++
                } else {
                    res[index] = nums2[r]
                    r--
                }
            } else {
                // We know the minimum first
                if nums2[l]<nums2[r] {
                    res[index] = nums2[l]
                    l++
                } else {
                    res[index] = nums2[r]
                    r--
                }
            }
            index += offset
        }
        return res
    }