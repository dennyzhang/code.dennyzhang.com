# Leetcode: Majority Element II     :BLOG:Hard:


---

Identity number which appears exactly once.  

---

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/majority-element-ii)  

Credits To: [Leetcode.com](https://leetcode.com/problems/majority-element-ii/description/)  

Hint: Time O(n), Space O(1)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            ## Basic Idea:
            ##       No more than 2 elements would be qualified.
            ## Complexity: Time O(n), Space O(1)
            ## Sample Data:
            ##    1 2 3 2 3 3
            ## Asummption: