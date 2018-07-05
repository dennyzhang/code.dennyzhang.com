
# Leetcode: Power of Two     :BLOG:Medium:

---

Given an integer, write a function to determine if it is a power of two.  

---

Similar Problems:  

-   [Review: Math Problems,](https://code.dennyzhang.com/review-math) Tag: [math](https://code.dennyzhang.com/tag/math)

---

Given an integer, write a function to determine if it is a power of two.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/power-of-two)  

Credits To: [leetcode.com](https://leetcode.com/problems/power-of-two/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/power-of-two
    class Solution(object):
        def isPowerOfTwo(self, n):
    	"""
    	:type n: int
    	:rtype: bool
    	"""
    	if n <= 0:
    	    return False
    	return n & (n-1) == 0

