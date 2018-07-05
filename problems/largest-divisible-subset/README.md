
# Leetcode: Largest Divisible Subset     :BLOG:Medium:

---

Largest Divisible Subset  

---

Similar Problems:  

-   Tag: [#array](https://code.dennyzhang.com/tag/array), [#math](https://code.dennyzhang.com/tag/math), [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.  

If there are multiple solutions, return any subset is fine.  

Example 1:  

    nums: [1,2,3]
    
    Result: [1,2] (of course, [1,3] will also be ok)

Example 2:  

    nums: [1,2,4,8]
    
    Result: [1,2,4,8]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/largest-divisible-subset)  

Credits To: [leetcode.com](https://leetcode.com/problems/largest-divisible-subset/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: dynamic programming

**Key Observations:**  

    If Si>Sj, then Sj%Si != 0.

**Walk Through Testdata**  

    nums: 1 2 5 10 15 30 31
    dp:   1 2 2 3  3  4  2
    result: 30->15->5->1: [1, 5, 15, 30]

    // Blog link: https://code.dennyzhang.com/largest-divisible-subset
    // Basic Ideas: Dynamic Programming
    // Complexity: Time O(n*n), Space O(n)
    func largestDivisibleSubset(nums []int) []int {
        if len(nums) == 0 { return []int{} }
        sort.Ints(nums)
        dp := make([]int, len(nums))
        for i:= 0; i<len(nums); i++ { dp[i] = 1 }
    
        max_index := 0
        for i:= 1; i<len(nums); i++ {
    	count := 1
    	for j:= i-1; j>=0; j-- {
    	    if nums[i] % nums[j] == 0 {
    		if dp[j]+1 > count {  count = dp[j]+1 }
    	    }
    	}
    	dp[i] = count
    	if count > dp[max_index] { max_index = i }
        }
    
        res := []int{}
        res = append([]int{nums[max_index]}, res...)
        for i := max_index-1; i>=0; i-- {
    	if dp[i]+1 == dp[max_index] && nums[max_index] % nums[i] == 0 {
    	    max_index = i
    	    res = append([]int{nums[max_index]}, res...)
    	}
        }
        return res
    }

