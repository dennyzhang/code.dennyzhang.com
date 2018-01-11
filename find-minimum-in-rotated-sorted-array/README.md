# Leetcode: Find Minimum in Rotated Sorted Array     :BLOG:Amusing:


---

Find Minimum in Rotated Sorted Array  

---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.  

You may assume no duplicate exists in the array.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-minimum-in-rotated-sorted-array)  

Credits To: [Leetcode.com](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Binary search
    ##              Compare all values with the first element
    ##              If bigger, consider it as 1. Otherwise -1
    ##              The first -1 is the mininum element we want to find.
    ##              If none is found, the first element is the mininum element
    ## Complexity: 
    class Solution(object):
        def findMin(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length == 0:
                return None
            if length == 1:
                return nums[0]
            left, right = 1, length - 1
            while left <= right:
                mid = left + (right-left)/2
                v = nums[mid] - nums[0]
                if v > 0:
                    left = mid + 1
                else:
                    # since no duplicate, v must be negative now
                    right = mid - 1
            return nums[mid] if nums[mid] - nums[0] < 0 else nums[0]
    
    s = Solution()
    print s.findMin([4,5,1,2,3])