# Leetcode: Single Element in a Sorted Array     :BLOG:Amusing:


---

Identity number which appears exactly once.  

---

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.  

    Example 1:
    Input: [1,1,2,3,3,4,4,8,8]
    Output: 2

    Example 2:
    Input: [3,3,7,7,10,11,11]
    Output: 10

Note: Your solution should run in O(log n) time and O(1) space.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/single-element-in-a-sorted-array)  

Credits To: [Leetcode.com](https://leetcode.com/problems/single-element-in-a-sorted-array/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def singleNonDuplicate(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ## Basic Ideas: Binary search
            ##              Find the middle element.
            ##              If the middle is different from the both sides, that's what we want
            ##              If the middle is the same with one side, check whether the both the left and right part
            ##                 The target is in the part which has odd elements
            ##              Otherwise the right half
            ## Complexity: Time O(log(n)), Space O(1)
            ## Sample Data: [1,1,2,3,3,4,4,8,8]
            length = len(nums)
            left, right = 0, length - 1
            while left <= right:
                mid = (left+right)/2
                if mid == 0 or mid == length-1:
                    return nums[mid]
    
                if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                    return nums[mid]
                else:
                    if nums[mid] == nums[mid-1]:
                        left_count = mid-1-left
                        if left_count % 2 != 0:
                            right = mid - 2
                        else:
                            left = mid + 1
                    else:
                        left_count = mid-left
                        if left_count % 2 != 0:
                            right = mid -1
                        else:
                            left = mid + 2
            return None
    
    s = Solution()
    print s.singleNonDuplicate([1,1,2])
    print s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
    print s.singleNonDuplicate([3,3,7,7,10,11,11])
    print s.singleNonDuplicate()

More Reading:  
-   [Leetcode: Majority Element](http://brain.dennyzhang.com/majority-element/)