# Leetcode: 4Sum     :BLOG:Medium:


---

4Sum  

---

Similar Problems:  
-   [Tag: #twosum](https://brain.dennyzhang.com/tag/twosum)
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer)
-   [Review: Problems With Many Details](https://brain.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://brain.dennyzhang.com/tag/manydetails), [#twopointer](https://brain.dennyzhang.com/tag/twopointer)

---

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.  

Note: The solution set must not contain duplicate quadruplets.  

    For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
    
    A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/4sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/4sum/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/4sum
    class Solution(object):
        def fourSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            ## Idea: sort the list, then 4 indices. i, j, l, r
            ## Complexity: Time O(n*n*n), Space O(1)
            ## Sample Data:
            nums.sort()
            res = []
            for i in xrange(len(nums)-3):
                if i>0 and nums[i] == nums[i-1]:
                    continue
    
                for j in range(i+1, len(nums)-2):
                    if j>i+1 and nums[j] == nums[j-1]:
                        continue
    
                    l = j+1
                    r = len(nums)-1
                    while l<r:
                        val = nums[i] + nums[j] + nums[l] + nums[r]
                        if val > target:
                            r -= 1
                        elif val < target:
                            l += 1
                        else:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            while l<r and nums[l] == nums[l+1]:
                                l += 1
                            while l<r and nums[r] == nums[r-1]:
                                r -= 1
                            l, r = l+1, r-1
            return res