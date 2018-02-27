# Leetcode: Search in Rotated Sorted Array II     :BLOG:Medium:


---

Search in Rotated Sorted Array II  

---

Similar Problems:  
-   [Search in Rotated Sorted Array](https://brain.dennyzhang.com/search-in-rotated-sorted-array)
-   [Review: Binary Search Problems](https://brain.dennyzhang.com/review-binarysearch), [Tag: #binarysearch](https://brain.dennyzhang.com/tag/binarysearch)

---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).  

Write a function to determine if a given target is in the array.  

The array may contain duplicates.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/search-in-rotated-sorted-array-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/search-in-rotated-sorted-array-ii
    ## Basic Ideas: Binary search
    ##  Find the pivot. And do two binary search
    ## Complexity: Time O(log(n)), Space O(1)
    class Solution:
        def search(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: bool
            """
            length = len(nums)
            if length == 0: return False
            left, right = 0, length - 1
            while left<right:
                mid = left + int((right-left)/2)
                # 5 6 6 0 0 2 3
                if nums[mid] <= nums[right]:
                    # check the left half(included)
                    right = mid
                else:
                    # right half
                    left = mid + 1
    
            pivot = left
            print(pivot)
            # binary search for part1
            left, right = 0, pivot-1
            while left<=right:
                mid = left + int((right-left)/2)
                if nums[mid] == target: return True
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
    
            # binary search for part2
            left, right = pivot, length-1
            while left<=right:
                mid = left + int((right-left)/2)
                if nums[mid] == target: return True
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
    
            return False
    s = Solution()
    print(s.search([2,2,2,0,2,2], 0)) # True