# Leetcode: 3Sum Closest     :BLOG:Medium:


---

3Sum Closest  

---

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.  

    For example, given array S = {-1 2 1 -4}, and target = 1.
    
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/3sum-closest)  

Credits To: [Leetcode.com](https://leetcode.com/problems/3sum-closest/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def threeSumClosest(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            ## Idea: sort the list. target_sum, 3 indices: i, l, r
            ## Complexity:
            ## Sample Data
            nums.sort()
            if len(nums) < 3:
                return None
            res = nums[0] + nums[1] + nums[2]
            for i in xrange(len(nums)-2):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                l,r = i+1, len(nums)-1
                while l<r:
                    value = nums[i] + nums[l] + nums[r]
                    offset = abs(value - target)
                    if value == target:
                        return value
    
                    if abs(res - target) > offset:
                        res = value
    
                    if value > target:
                        r -= 1
                    if value < target:
                        l += 1
            return res