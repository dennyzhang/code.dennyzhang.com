# Leetcode: 3Sum Closest     :BLOG:Medium:


---

3Sum Closest  

---

Similar Problems:  
-   [3Sum Smaller](https://brain.dennyzhang.com/3sum-smaller)
-   [Tag: #twosum](https://brain.dennyzhang.com/tag/twosum)
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://brain.dennyzhang.com/tag/twopointer)

---

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.  

    For example, given array S = {-1 2 1 -4}, and target = 1.
    
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/3sum-closest)  

Credits To: [leetcode.com](https://leetcode.com/problems/3sum-closest/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/3sum-closest
    ## Basic Ideas: two sum
    ## Complexity: Time O(n*n), Space O(1)
    class Solution:
        def threeSumClosest(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            import sys
            length = len(nums)
            if length <=2: return sum(nums)
            nums.sort()
            res = sum(nums[0:3])
            for i in range(length-2):
                l, r = i+1, length-1
                while l<r:
                    v = nums[i]+nums[l]+nums[r]
                    if v == target: return v
                    if abs(v-target) < abs(res-target): res = v
    
                    if v > target:
                        # make v smaller
                        r -= 1
                    else:
                        l += 1
    
            return res