
# LintCode: A + B Problem     :BLOG:Medium:

---

A + B Problem  

---

Similar Problems:  

-   [Sum of Two Integers](https://code.dennyzhang.com/sum-of-two-integers)
-   [Tag: #bitmanipulation](https://code.dennyzhang.com/tag/bitmanipulation)

---

Write a function that add two numbers A and B. You should not use + or any arithmetic operators.  

Notice  
There is no need to read data from standard input stream. Both parameters are given in function aplusb, you job is to calculate the sum and return it.  

Clarification  
Are a and b both 32-bit integers?  

Yes.  
Can I use bit operation?  

Sure you can.  
Example  
Given a=1 and b=2 return 3  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/a-b-problem)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/a-b-problem/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/a-b-problem
    class Solution:
        """
        @param a: An integer
        @param b: An integer
        @return: The sum of a and b
        """
        def aplusb(self, a, b):
    	## Basic Ideas:
    	##
    	##   a ^ b: add without carry
    	##   (a & b) << 1: carry
    	##
    	##  Assumption: the result won't overflow
    	##
    	## Complexity: Time O(1), Space O(1)
    	mod = 0xFFFFFFFF
    	while b != 0:
    	    a, b = (a ^ b) & mod, ((a & b) << 1) & mod
    	return a

