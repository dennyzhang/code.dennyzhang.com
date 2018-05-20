# Leetcode: Search Insert Position     :BLOG:Basic:


---

Search Insert Position  

---

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  

You may assume no duplicates in the array.  

    Example 1:
    
    Input: [1,3,5,6], 5
    Output: 2

    Example 2:
    
    Input: [1,3,5,6], 2
    Output: 1

    Example 3:
    
    Input: [1,3,5,6], 7
    Output: 4

    Example 4:
    
    Input: [1,3,5,6], 0
    Output: 0

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/search-insert-position)  

Credits To: [leetcode.com](https://leetcode.com/problems/search-insert-position/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/search-insert-position
    class Solution(object):
        def searchInsert(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            i = 0
            for num in nums:
                if num >= target:
                    return i
                i = i + 1
            return i