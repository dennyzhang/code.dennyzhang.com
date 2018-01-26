# Leetcode: Remove Element     :BLOG:Basic:


---

Given an array and a value, remove all instances of that value in-place and return the new length.  

---

Given an array and a value, remove all instances of that value in-place and return the new length.  

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.  

The order of elements can be changed. It doesn't matter what you leave beyond the new length.  

Example:  

Given nums = [3,2,2,3], val = 3,  

Your function should return length = 2, with the first two elements of nums being 2.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-element)  

Credits To: [leetcode.com](https://leetcode.com/problems/remove-element/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/remove-element
    ## Basic Ideas:
    ##        index point to the last element which have been processed
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def removeElement(self, nums, val):
            """
            :type nums: List[int]
            :type val: int
            :rtype: int
            """
            index = 0
            for n in nums:
                if n != val:
                    nums[index] = n
                    index += 1
            return index