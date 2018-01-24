# Leetcode: Find Minimum in Rotated Sorted Array     :BLOG:Amusing:


---

Find Minimum in Rotated Sorted Array  

---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.  

You may assume no duplicate exists in the array.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-minimum-in-rotated-sorted-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/find-minimum-in-rotated-sorted-array
    ## Basic Ideas: Binary search: find the first negative
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
                    # right part
                    left = mid + 1
                else:
                    # since no duplicate, v must be negative now
                    if mid == 1 or mid == length -1:
                        return nums[mid]
                    left_element = nums[mid-1]
                    if left_element > nums[0]:
                        return nums[mid]
                    else:
                        # left part
                        right = mid - 1
    
            return nums[0]
    
    s = Solution()
    print s.findMin([4,5,1,2,3]) #1
    print s.findMin([1,2]) #1