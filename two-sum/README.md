# Leetcode: Two Sum     :BLOG:Basic:


---

Pic 2 numbers to get the target sum.  

---

Similar Problems:  
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://brain.dennyzhang.com/tag/twopointer)

---

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.  

You may assume that each input would have **exactly** one solution, and you may not use the same element twice.  

Example:  

    Given nums = [2, 7, 11, 15], target = 9,
    
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/two-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/two-sum/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/two-sum
    ## Basic Ideas: Sort, then two pointer
    ##
    ## Complexity: Time O(n*log(n)), Space O(1)
    class Solution:
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            l = sorted(zip(nums, range(len(nums))))
            left, right = 0, len(l)-1
            while left<right:
                v = l[left][0]+l[right][0]
                if v == target:
                    return [l[left][1], l[right][1]]
                if v < target:
                    left += 1
                else:
                    right -= 1