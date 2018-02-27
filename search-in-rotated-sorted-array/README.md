# Leetcode: Search in Rotated Sorted Array     :BLOG:Medium:


---

Search in Rotated Sorted Array  

---

Similar Problems:  
-   [Find Minimum in Rotated Sorted Array](https://brain.dennyzhang.com/find-minimum-in-rotated-sorted-array)
-   [Review: Binary Search Problems](https://brain.dennyzhang.com/review-binarysearch), [Tag: #binarysearch](https://brain.dennyzhang.com/tag/binarysearch)

---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).  

You are given a target value to search. If found in the array return its index, otherwise return -1.  

You may assume no duplicate exists in the array.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/search-in-rotated-sorted-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/search-in-rotated-sorted-array
    ## Basic Ideas: Binary search
    ##  Find the pivot. And do two binary search
    ## Complexity: Time O(log(n)), Space O(1)
    class Solution:
        def search(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            length = len(nums)
            if length == 0: return -1
            left, right = 0, length - 1
            while left<right:
                mid = left + int((right-left)/2)
                # 5 6 7 0 1 2 3
                if nums[mid] < nums[right]:
                    # check the left half(included)
                    right = mid
                else:
                    left = mid + 1
    
            pivot = left
            # binary search for part1
            left, right = 0, pivot-1
            while left<=right:
                mid = left + int((right-left)/2)
                if nums[mid] == target: return mid
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
    
            # binary search for part2
            left, right = pivot, length-1
            while left<=right:
                mid = left + int((right-left)/2)
                if nums[mid] == target: return mid
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
    
            return -1