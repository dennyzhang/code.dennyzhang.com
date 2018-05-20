# Leetcode: Climbing Stairs     :BLOG:Amusing:


---

Simple DP  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

You are climbing a stair case. It takes n steps to reach to the top.  

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?  

Note: Given n will be a positive integer.  

Example 1:  

    Input: 2
    Output:  2
    Explanation:  There are two ways to climb to the top.
    
    1. 1 step + 1 step
    2. 2 steps

Example 2:  

    Input: 3
    Output:  3
    Explanation:  There are three ways to climb to the top.
    
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/climbing-stairs)  

Credits To: [leetcode.com](https://leetcode.com/problems/climbing-stairs/description/)  

Hint: Time O(n), Space O(1)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/climbing-stairs
    ## Basic Ideas: fibonacci
    class Solution(object):
        def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n == 1:
                return 1
            if n == 2:
                return 2
            value1 = 1
            value2 = 2
            for i in range(3, n):
                value = value2
                value2 = value1 + value2
                value1 = value
            return value1 + value2