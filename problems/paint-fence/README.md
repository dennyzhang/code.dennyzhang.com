
# Leetcode: Paint Fence     :BLOG:Medium:

---

Paint Fence  

---

Similar Problems:  

-   [Climbing Stairs](https://code.dennyzhang.com/climbing-stairs)
-   [House Robber](https://code.dennyzhang.com/house-robber)
-   [Paint House](https://code.dennyzhang.com/paint-house)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

There is a fence with n posts, each post can be painted with one of the k colors.  

You have to paint all the posts such that no more than two adjacent fence posts have the same color.  

Return the total number of ways you can paint the fence.  

Note:  
n and k are non-negative integers.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/paint-fence)  

Credits To: [leetcode.com](https://leetcode.com/problems/paint-fence/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/paint-fence
    ## Basic Ideas: Dynamic programming
    ##     To get f(n), it can only have two cases:
    ##           Fence nth uses the same color as fence n-1 th: f(n-1)*(k-1)
    ##                     Uses a different color: f(n-2)*(k-1)
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def numWays(self, n, k):
    	"""
    	:type n: int
    	:type k: int
    	:rtype: int
    	"""
    	if k == 0 or n == 0: return 0
    	if k == 1: return 1 if n<=2 else 0
    	if n == 1: return k
    	if n == 2: return k*k
    	value1, value2 = k, k*k
    	for i in range(3, n+1):
    	    v = (value1+value2)*(k-1)
    	    value1, value2 = value2, v
    	return value2

