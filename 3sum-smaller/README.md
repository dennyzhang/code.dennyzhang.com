# Leetcode: 3Sum Smaller     :BLOG:Medium:


---

3Sum Smaller  

---

Similar Problems:  
-   [3Sum Closest](https://code.dennyzhang.com/3sum-closest)
-   [Tag: #twosum](https://code.dennyzhang.com/tag/twosum)
-   [Review: TwoPointers Problems](https://code.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.  

For example, given nums = [-2, 0, 1, 3], and target = 2.  

Return 2. Because there are two triplets which sums are less than 2:  

    [-2, 0, 1]
    [-2, 0, 3]

Follow up:  
Could you solve it in O(n^2) runtime?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/3sum-smaller)  

Credits To: [leetcode.com](https://leetcode.com/problems/3sum-smaller/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/3sum-smaller
    ## Basic Ideas: two pointer
    ## Complexity: Time O(n*n), Space O(1)
    class Solution:
        def threeSumSmaller(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            nums.sort()
            length = len(nums)
            res = 0
            for i in range(0, length-2):
                l, r = i+1, length-1
                while l<r:
                    v = nums[i]+nums[l]+nums[r]
                    if v < target:
                        res += (r-l)
                        l += 1
                    else:
                        r -= 1
            return res