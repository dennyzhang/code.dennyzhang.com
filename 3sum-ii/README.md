
# LintCode: 3Sum II     :BLOG:Medium:

---

3Sum II  

---

Similar Problems:  

-   [Sum of Square Numbers](https://code.dennyzhang.com/sum-of-square-numbers)
-   [Tag: #twosum](https://code.dennyzhang.com/tag/twosum)
-   [Review: TwoPointers Problems](https://code.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Given n, find the number of solutions for all x, y, z that conforms to x^2+y^2+z^2 = n.(x, y, z are non-negative integers)  

Notice  

-   n <= 1000000
-   x, y, z satisfy (x <= y <= z), we can consider that is the same solution as long as the three numbers selected are the same

Example  

    Given n = 0, return 1.
    
    Explanation:
    When x = 0, y = 0, z = 0, the equation holds.

    Given n = 1, return 1.
    
    Explanation:
    When one of them is 1 and the remaining two are 0, there is a total of 1 solution.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/3sum-ii)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/3sum-ii/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/3sum-ii
    class Solution:
        """
        @param n: an integer
        @return: the number of solutions
        """
        def threeSum2(self, n):
    	## Basic Ideas:
    	## Complexity: Time O(n*n), Space O(1)
    	import math
    	nums = [x*x for x in range(1001)]
    	res = 0
    
    	max = int(math.sqrt(n))
    	for i in range(max+1):
    	    l, r = i, max
    	    while l<=r:
    		v = nums[i]+nums[l]+nums[r]
    		if v == n:
    		    res += 1
    		    l += 1
    		elif v>n:                
    		    r -= 1
    		else:
    		    l += 1
    	return res

