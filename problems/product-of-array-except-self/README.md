
# Leetcode: Product of Array Except Self     :BLOG:Medium:

---

Product of Array Except Self  

---

Similar Problems:  

-   [Shortest Distance to a Character](https://code.dennyzhang.com/shortest-distance-to-a-character)
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#array](https://code.dennyzhang.com/tag/array), [#twopass](https://code.dennyzhang.com/tag/twopass), [#classic](https://code.dennyzhang.com/tag/classic)

---

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].  

Example:  

    Input:  [1,2,3,4]
    Output: [24,12,8,6]

Note: Please solve it without division and in O(n).  

Follow up:  
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/product-of-array-except-self)  

Credits To: [leetcode.com](https://leetcode.com/problems/product-of-array-except-self/description/)  

Leave me comments, if you have better ways to solve.  

---

Similar problem: [Trapping Rain Water](https://code.dennyzhang.com/trapping-rain-water)  

-   Solution:

**General Thinkings:**  

    Two pass: 
    - From left to right, get partial results. 
    - Then from right to left, get final results.

We can use the similar two-pass idea to solve: [Shortest Distance to a Character](https://code.dennyzhang.com/shortest-distance-to-a-character)  

**Walk Through Testdata**  

    // Numbers:     2    3    4     5
    // Lefts:            2  2*3 2*3*4
    // Rights:  3*4*5  4*5    5      
    // Let's fill the empty with 1:
    
    // Numbers:     2    3    4     5
    // Lefts:       1    2  2*3 2*3*4
    // Rights:  3*4*5  4*5    5     1

    // Blog link: https://code.dennyzhang.com/product-of-array-except-self
    // Basic Ideas:
    //
    // Complexity: Time O(n), Space O(1)
    func productExceptSelf(nums []int) []int {
        res := make([]int, len(nums))
        res[0] = 1
        for product, i:=1, 1; i<len(nums); i++ {
    	product *= nums[i-1]
    	res[i] = product
        }
        for product, i:=1, len(nums)-2; i>=0; i-- {
    	product *= nums[i+1]
    	res[i] *= product
        }
        return res
    }

