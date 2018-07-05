
# Leetcode: House Robber     :BLOG:Medium:

---

House Robber  

---

Similar Problems:  

-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/house-robber)  

Credits To: [leetcode.com](https://leetcode.com/problems/house-robber/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/house-robber
    class Solution(object):
        def rob(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: int
    	"""
    	## Idea: Recursive way will timeout
    	##       DP: robs[i] the max profit so far.
    	##       How does DP formula work?
    	## Complexity:
    	length = len(nums)
    	if length == 0:
    	    return 0
    	if length == 1:
    	    return nums[0]
    	if length == 2:
    	    return max(nums[0], nums[1])
    
    	robs = [None]*length
    	robs[0] = nums[0]
    	robs[1] = max(nums[0], nums[1])
    	robs[2] = max(nums[0]+nums[2], nums[1])
    
    	for i in range(3, length):
    	    robs[i] = max(robs[i-3]+nums[i-1], robs[i-2]+nums[i])
    	return robs[-1]

