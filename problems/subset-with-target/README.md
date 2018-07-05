
# LintCode: Subset With Target     :BLOG:Medium:

---

Subset With Target  

---

Similar Problems:  

-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination), [Tag: #combination](https://code.dennyzhang.com/tag/combination)

---

Give an array and a target. We need to find the number of subsets which meet the following conditions:  
The sum of the minimum value and the maximum value in the subset is less than the target.  

Notice  

-   The length of the given array does not exceed 50.
-   target <= 100000.

Example  
Give array = [1,5,2,4,3], target = 4, return 2.  

    Explanation:
    Only subset [1],[1,2] satisfy the condition, so the answer is 2.
    Give array = [1,5,2,4,3],target = 5, return 5.

    Explanation:
    Only subset [1],[2],[1,3],[1,2],[1,2,3] satisfy the condition, so the answer is 5.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/subset-with-target)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/subset-with-target/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/subset-with-target
    #!/usr/bin/env python
    class Solution:
        """
        @param nums: the array
        @param target: the target
        @return: the number of subsets which meet the following conditions
        """
        ## Basic Ideas: Two pointers
        ## Complexity: Time O(n*log(n)), Space O(n)
        def subsetWithTarget(self, nums, target):
    	nums.sort()
    	res = 0
    	left, right = 0, len(nums)-1
    	while left <= right:
    	    v = nums[left] + nums[right]
    	    if v >= target:
    		right -= 1
    		continue
    	    # whether we can choose the left
    	    res += pow(2, (right-left))
    	    left += 1
    	return res
    
    # s = Solution()
    # print(s.subsetWithTarget([1, 5, 2, 4, 3], 5)) # 5

