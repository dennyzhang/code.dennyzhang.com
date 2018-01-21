# Leetcode: Summary Ranges     :BLOG:Basic:


---

Combine ranges  

---

Given a sorted integer array without duplicates, return the summary of its ranges.  

    Example 1:
    Input: [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]

    Example 2:
    Input: [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/summary-ranges)  

Credits To: [leetcode.com](https://leetcode.com/problems/summary-ranges/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/summary-ranges
    ## Basic Ideas: 2 pointer
    ## Complexity: Time O(n), Space O(1)
    ## Assumptions:
    class Solution(object):
        def summaryRanges(self, nums):
            """
            :type nums: List[int]
            :rtype: List[str]
            """
            res = []
            length = len(nums)
            i=0
            while i<length:
                j = i + 1
                while j<length and nums[j] == nums[j-1] + 1:
                    j += 1
                if j != i+1:
                    res.append("%d->%d" % (nums[i], nums[j-1]))
                else:
                    res.append("%d" % nums[i])
                i = j
            return res