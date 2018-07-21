
# Leetcode: Implement Rand10() Using Rand7()     :BLOG:Medium:

---

Implement Rand10() Using Rand7()  

---

Similar Problems:  

-   [Leetcode: Random Pick with Blacklist](https://code.dennyzhang.com/random-pick-with-blacklist)
-   Tag: [#random](https://code.dennyzhang.com/tag/random), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.  

Do NOT use system's Math.random().  

Example 1:  

    Input: 1
    Output: [7]

Example 2:  

    Input: 2
    Output: [8,4]

Example 3:  

    Input: 3
    Output: [8,1,10]

Note:  

1.  rand7 is predefined.
2.  Each testcase has one argument: n, the number of times that rand10 is called.

Follow up:  

-   What is the expected value for the number of calls to rand7() function?
-   Could you minimize the number of calls to rand7()?

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/implement-rand10-using-rand7)  

Credits To: [leetcode.com](https://leetcode.com/problems/implement-rand10-using-rand7/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    ## Blog link: https://code.dennyzhang.com/implement-rand10-using-rand7
    ## Basic Ideas:
    ##  f(7) -> f(49) -> f(40) -> f(10)
    ##    0 - 48: 6*x+y
    ##    0 - 39
    ##       0, 10, 20, 30 -> 0
    ##       1, 11, 21, 31 -> 1
    ##       2, 12, 22, 32 -> 2
    ##       ...
    ##    0 - 9
    ##    1 - 10
    ## Complexity:
    # The rand7() API is already defined for you.
    # def rand7():
    # @return a random integer in the range 1 to 7
    class Solution:
        def rand10(self):
    	"""
    	:rtype: int
    	"""
    	res = 40
    	while res>=40:
    	    res = 7*(rand7()-1) + (rand7()-1)
    	return res%10+1

