
# Leetcode: Search in Rotated Sorted Array II     :BLOG:Medium:

---

Search in Rotated Sorted Array II  

---

Similar Problems:  

-   [Search in Rotated Sorted Array](https://code.dennyzhang.com/search-in-rotated-sorted-array)
-   [Review: Binary Search Problems](https://code.dennyzhang.com/review-binarysearch)
-   Tag: [#binarysearch](https://code.dennyzhang.com/tag/binarysearch), [#rotateoperation](https://code.dennyzhang.com/tag/rotateoperation)

---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).  

Write a function to determine if a given target is in the array.  

The array may contain duplicates.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/search-in-rotated-sorted-array-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/search-in-rotated-sorted-array-ii
    ## Basic Ideas: The worst case would be: 1111112, then you need to check 2 or 3
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def search(self, nums, target):
    	"""
    	:type nums: List[int]
    	:type target: int
    	:rtype: bool
    	"""
    	for num in nums:
    	    if num == target: return True
    	return False

