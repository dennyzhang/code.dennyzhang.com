# Leetcode: Integer Break     :BLOG:Medium:


---

Integer Break  

---

Similar Problems:  
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#math](https://code.dennyzhang.com/tag/math)

---

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.  

    For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/integer-break)  

Credits To: [leetcode.com](https://leetcode.com/problems/integer-break/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/integer-break
    // Basic Ideas: dynamic programming
    //
    // dp(i)
    //    break i as j, k. So i = j+k
    // dp(i) = max(
    //          max(1, dp(1))*max(i-1, *dp(i-1)),
    //          max(2, dp(2))*max(i-2, *dp(i-2)), 
    //          max(3, dp(3))*max(i-3, *dp(i-3)), 
    //          max(4, dp(4))*max(i-4, *dp(i-4)),
    // ...      max(j, dp(j))*max(i-j, *dp(i-j)), (j<=int(i/2))
    //
    // Complexity: Time O(n*n), Space O(n)
    func integerBreak(n int) int {
      if n == 1 { return 0 }
      if n == 2 { return 1 }
      dp := make([]int, n+1)
      dp[0], dp[1], dp[2] = 0, 0, 1
      for i:=3; i<=n; i++ {
        max_product := 0
        for j:=1; j<=int(i/2); j++ {
          v1, v2 := dp[j], dp[i-j]
          if v1<j { v1=j }
          if v2<i-j { v2=i-j }
          if v1*v2>max_product { max_product = v1*v2 }
        }
        dp[i] = max_product
      }
      return dp[n]
    }