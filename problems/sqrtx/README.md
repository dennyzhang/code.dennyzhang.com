
# Leetcode: Sqrt(x)     :BLOG:Medium:

---

Implement int sqrt(int x).  

---

Similar Problems:  

-   [Review: Binary Search Problems](https://code.dennyzhang.com/review-binarysearch)
-   [Review: sqrt Problems](https://code.dennyzhang.com/review-sqrt)
-   Tag: [#binarysearch](https://code.dennyzhang.com/tag/binarysearch), [sqrt](https://code.dennyzhang.com/tag/sqrt)

---

Implement int sqrt(int x).  

Compute and return the square root of x.  

x is guaranteed to be a non-negative integer.  

    Example 1:
    
    Input: 4
    Output: 2

    Example 2:
    
    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/sqrtx)  

Credits To: [leetcode.com](https://leetcode.com/problems/sqrtx/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/sqrtx
    ## Basic Ideas: Binary search
    ##              Check [1^2, 2^2, 3^2, ... n^2]
    ## Complexity: Time O(log(n)), Space O(1)
    class Solution(object):
        def mySqrt(self, x):
    	"""
    	:type x: int
    	:rtype: int
    	"""
    	if x == 0:
    	    return 0
    	left, right = 1, x
    	while left <= right:
    	    mid = left + (right-left)/2
    	    v = mid * mid
    	    if v == x:
    		return mid
    	    elif v < x:
    		left = mid + 1
    	    else:
    		right = mid - 1
    	return right

