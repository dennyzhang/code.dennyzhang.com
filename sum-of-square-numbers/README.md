# Leetcode: Sum of Square Numbers     :BLOG:Medium:


---

Sum of Square Numbers  

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

Credits To: [Leetcode.com](https://leetcode.com/problems/sum-of-square-numbers/description/)  

Leave me comments, if you know how to solve.  

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