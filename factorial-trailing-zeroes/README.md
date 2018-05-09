# Leetcode: Factorial Trailing Zeroes     :BLOG:Amusing:


---

Factorial Trailing Zeroes  

---

Similar Problems:  
-   [Number of Digit One](https://code.dennyzhang.com/number-of-digit-one)
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   Tag: [math](https://code.dennyzhang.com/tag/math), [inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given an integer n, return the number of trailing zeroes in n!.  

Note: Your solution should be in logarithmic time complexity.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/factorial-trailing-zeroes)  

Credits To: [leetcode.com](https://leetcode.com/problems/factorial-trailing-zeroes/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/factorial-trailing-zeroes
    // Basic Ideas:
    //  Count how many 5 factors in all number from 1 to n.
    //  We have enough 2 to get 10
    //
    // Complexity: Time O(log(n)), Space O(1)
    func trailingZeroes(n int) int {
        res := 0
        for n%5 == 0 {
            n = int(n/5)
            res += 1
        }
        return res
    }