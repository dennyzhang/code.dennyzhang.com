# Leetcode: Longest Continuous Increasing Subsequence     :BLOG:Basic:


---

Longest Continuous Increasing Subsequence  

---

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).  

    Example 1:
    Input: [1,3,5,4,7]
    Output: 3
    Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
    Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

    Example 2:
    Input: [2,2,2,2,2]
    Output: 1
    Explanation: The longest continuous increasing subsequence is [2], its length is 1.

Note: Length of the array will not exceed 10,000.  

Blog link: <http://brain.dennyzhang.com/longest-continuous-increasing-subsequence>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-continuous-increasing-subsequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: bigger_count: point to how many continuous increasing subsequence
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def findLengthOfLCIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # empty or one element
            if len(nums) <= 1:
                return len(nums)
    
            bigger_count, res = 1, 1
            for i in range(1, len(nums)):
                # print("bigger_count: %d, nums[i]: %d, res: %d" % (bigger_count, nums[i], res))
                if nums[i] > nums[i-1]:
                    bigger_count += 1
                else:
                    res = max(bigger_count, res)
                    bigger_count = 1
            return max(bigger_count, res)
    
    s = Solution()
    print s.findLengthOfLCIS([1,3,5,7]) # 4
    print s.findLengthOfLCIS([1,3,5,4,7]) # 3
    print s.findLengthOfLCIS([2, 2, 2, 2]) # 1