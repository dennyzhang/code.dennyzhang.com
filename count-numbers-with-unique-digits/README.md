# Leetcode: Count Numbers with Unique Digits     :BLOG:Medium:


---

Count Numbers with Unique Digits  

---

Similar Problems:  
-   [Number of Digit One](https://code.dennyzhang.com/number-of-digit-one)
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   Tag: [math](https://code.dennyzhang.com/tag/math)

---

Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.  

Example:  

    Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/count-numbers-with-unique-digits)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-numbers-with-unique-digits/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/count-numbers-with-unique-digits
    // Basic Ideas: dynamic programming
    //   dp(i): How many unique digits with length of i
    //
    // Complexity: Time O(n*n), Space O(1)
    func countNumbersWithUniqueDigits(n int) int {
        if n == 0 { return 1 }
        if n == 1 { return 10 }
        res := 10
        for i:=2; i<=n; i++ {
            count := 9
            for j := i-1; j>=1; j-- {
                count = count * (10-j)
            }
            res += count
        }
        return res
    }