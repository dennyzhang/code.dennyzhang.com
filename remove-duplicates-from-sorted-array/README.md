# Leetcode: Remove Duplicates from Sorted Array     :BLOG:Medium:


---

Remove Duplicates from Sorted Array  

---

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.  

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.  

    Example:
    
    Given nums = [1,1,2],
    
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.

Blog link: <http://brain.dennyzhang.com/remove-duplicates-from-sorted-array>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-duplicates-from-sorted-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if len(nums) == 0:
                return 0
    
            ret = 0
            for i in range(0, len(nums)-1):
                if nums[i] != nums[i+1]:
                    ret += 1
                    nums[ret] = nums[i+1]
                i += 1
            return (ret + 1)