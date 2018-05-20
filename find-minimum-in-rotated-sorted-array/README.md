# Leetcode: Find Minimum in Rotated Sorted Array     :BLOG:Amusing:


---

Find Minimum in Rotated Sorted Array  

---

Similar Problems:  
-   [Search in Rotated Sorted Array](https://code.dennyzhang.com/search-in-rotated-sorted-array)
-   [Review: Binary Search Problems](https://code.dennyzhang.com/review-binarysearch)
-   Tag: [#binarysearch](https://code.dennyzhang.com/tag/binarysearch), [#rotateoperation](https://code.dennyzhang.com/tag/rotateoperation)

---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.  

You may assume no duplicate exists in the array.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-minimum-in-rotated-sorted-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/find-minimum-in-rotated-sorted-array
    class Solution:
        ## Basic Ideas: Binary Search
        ##   Check current node with the right node of the range
        ##   If it's smaller, check left half(included). Check the right half(excluded)
        ##
        ##   Notice: Here we can't compare it with the left node of the range.
        ##      Why? (0+1)/2 == 0. We might run into dead loop with left == mid.
        ##
        ## Complexity: Time O(log(n)), Space O(1)
        def findMin(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length == 0: return None
            # 4 5 6 7 0 1 2
            left, right = 0, length-1
            while left<right:
                mid = left + (int)((right-left)/2)
                if nums[mid] < nums[right]:
                    # check the left half(included)
                    right = mid
                else:
                    # check the right half(excluded)
                    left = mid + 1
            return nums[left]
    
        ## Basic Ideas: Binary Search
        ##     Find the first element, who is smaller than the first element
        ##     If not found, the first element is the target
        ##
        ## Complexity: Time O(log(n)), Space O(1)
        def findMin_v1(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length == 0: return None
            if length == 1: return nums[0]
    
            if nums[0] < nums[-1]: return nums[0]
            left, right = 1, length-1
            # 4 5 6 7 0 1 2
            while left < right:
                mid = left + (int)((right-left)/2)
                if nums[mid] < nums[0]:
                    right = mid
                else:
                    left = mid + 1
            return nums[left]