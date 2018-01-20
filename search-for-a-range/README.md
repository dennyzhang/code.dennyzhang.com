# Leetcode: Search for a Range     :BLOG:Hard:


---

Search for a Range  

---

Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.  

Blog link: <http://brain.dennyzhang.com/search-for-a-range>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/search-for-a-range)  

Credits To: [leetcode.com](https://leetcode.com/problems/search-for-a-range/description)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Find the left same, then the right same
    ## Complexity: Time O(log(n)), Space O(1)
    ## Assumptions:
    ## Sample Data:
    ##    5, 7, 7, 8, 8, 10
    ##             8
    ## binary search: 3 cases of not found
    ##           right mid(left)
    ##                mid(right) left
    class Solution(object):
        def searchRange(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            length = len(nums)
            left, right = 0, length - 1
            while left <= right:
                mid = left + (right-left)/2
                if nums[mid] >= target:
                    # left half
                    right = mid - 1
                else:
                    left = mid + 1
    
            # print("round1 mid: %d, left: %d, right: %d. nums: %s" % (mid, left, right, nums))
    
            left_index = min(left, right) + 1
            if left_index >= length:
                return [-1, -1]
            if nums[left_index] != target:
                return [-1, -1]
    
            left, right = 0, length - 1
            while left <= right:
                mid = left + (right-left)/2
                if nums[mid] <= target:
                    # right half
                    left = mid + 1
                else:
                    right = mid - 1
    
            # print("round2 mid: %d, left: %d, right: %d. nums: %s" % (mid, left, right, nums))
            right_index = min(left, right)
            return [left_index, right_index]
    
    s = Solution()
    print s.searchRange([5,7,7,8,8,8,10], 8)