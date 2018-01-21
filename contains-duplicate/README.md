# Leetcode: Contains Duplicate     :BLOG:Basic:


---

Contains Duplicate  

---

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/contains-duplicate)  

Credits To: [leetcode.com](https://leetcode.com/problems/contains-duplicate/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/contains-duplicate
    ## Complexity: Time O(n*log(n)), Space O(n)
    class Solution(object):
        def containsDuplicate(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            return len(nums) != len(set(nums))