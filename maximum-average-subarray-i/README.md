# Leetcode: Maximum Average Subarray I     :BLOG:Basic:


---

Maximum Average Subarray I  

---

Similar Problems:  
-   [Review: Greedy Problems](https://code.dennyzhang.com/review-greedy)
-   Tag: [#greedy](https://code.dennyzhang.com/tag/greedy), [#slidingwindow](https://code.dennyzhang.com/tag/slidingwindow), [#classic](https://code.dennyzhang.com/tag/classic)

---

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.  

Example 1:  

    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75
    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:  
1.  1 <= k <= n <= 30,000.
2.  Elements of the given array will be in the range [-10,000, 10,000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximum-average-subarray-i)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximum-average-subarray-i/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/maximum-average-subarray-i
    ## Basic Ideas: greedy + Sliding window
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def findMaxAverage(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: float
            """
            length = len(nums)
            if length <= k: return float(sum(nums))/k
    
            curSum = sum(nums[0:k])
            maxSum = curSum
            for i in range(k, length):
                curSum += nums[i] - nums[i-k]
                maxSum = max(maxSum, curSum)
    
            return float(maxSum)/k