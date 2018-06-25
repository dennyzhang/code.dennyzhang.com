# Leetcode: Sum of Square Numbers     :BLOG:Medium:


---

Sum of Square Numbers  

---

Similar Problems:  
-   [LintCode: 3Sum II](https://code.dennyzhang.com/3sum-ii)
-   [Tag: #twosum](https://code.dennyzhang.com/tag/twosum)
-   [Review: TwoPointers Problems](https://code.dennyzhang.com/review-twopointer)
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   [Review: sqrt Problems](https://code.dennyzhang.com/review-sqrt)
-   Tag: [#math](https://code.dennyzhang.com/tag/math), [#twopointer](https://code.dennyzhang.com/tag/twopointer), [sqrt](https://code.dennyzhang.com/tag/sqrt)

---

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a\*a + b\*b = c.  

    Example 1:
    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5

    Example 2:
    Input: 3
    Output: False

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sum-of-square-numbers)  

Credits To: [leetcode.com](https://leetcode.com/problems/sum-of-square-numbers/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/sum-of-square-numbers
    ## Basic Ideas: max(a, b) <= int(sqrt(c))
    ##              Then we convert it into a two-sum problem
    ##
    ##  Assumption: a, b can be 0
    ## Complexity: Time O(sqrt(n)), Space O(1)
    class Solution(object):
        def judgeSquareSum(self, c):
            """
            :type c: int
            :rtype: bool
            """
            if c < 0:
                return False
            import math
            a, b = 0, int(math.sqrt(c))
            # a may equals b
            while a <= b:
                v = a*a + b*b
                if v == c:
                    return True
                elif v > c:
                    b -= 1
                else:
                    a += 1
            return False