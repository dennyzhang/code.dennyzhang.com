# Leetcode: Sum of Two Integers     :BLOG:Hard:


---

Sum of two integers without using + or -  

---

Similar Problems:  
-   [LintCode: A + B Problem](https://code.dennyzhang.com/a-b-problem)
-   [Tag: #bitmanipulation](https://code.dennyzhang.com/tag/bitmanipulation)
-   [Review: Math Problems,](https://code.dennyzhang.com/review-math) Tag: [math](https://code.dennyzhang.com/tag/math)

---

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.  

Example:  
Given a = 1 and b = 2, return 3.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sum-of-two-integers)  

Credits To: [leetcode.com](https://leetcode.com/problems/sum-of-two-integers/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/sum-of-two-integers
    ## Basic Ideas: a xor b: get sum without carry. (a & b) << 1 carry
    ## Complexity:
    ## Sample data:
    ##       9
    ##       5
    ##     8 4 2 1
    ##     1 0 0 1
    ##     0 1 0 1
    ##
    ## res 1 1 1 0
    ##
    ## or  1 1 0 1
    ## and 0 0 0 1
    ## xor 1 1 0 0
    ##
    ##     8 4 2 1
    ##     0 0 1 0
    ##     0 0 1 1
    ##
    ##     0 1 0 0
    ##     0 0 0 1
    class Solution(object):
        def getSum(self, a, b):
            """
            :type a: int
            :type b: int
            :rtype: int
            """
            MOD     = 0xFFFFFFFF
            MAX_INT = 0x7FFFFFFF
            while b!= 0:
                c = a & b
                a = (a ^ b) & MOD
                b = (c << 1) & MOD
            return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT