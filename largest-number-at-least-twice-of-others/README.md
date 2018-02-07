# Leetcode: Largest Number At Least Twice of Others     :BLOG:Easy:


---

Largest Number At Least Twice of Others  

---

In a given integer array nums, there is always exactly one largest element.  

Find whether the largest element in the array is at least twice as much as every other number in the array.  

If it is, return the index of the largest element, otherwise return -1.  

Example 1:  

    Input: nums = [3, 6, 1, 0]
    Output: 1
    Explanation: 6 is the largest integer, and for every other number in the array x,
    6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:  

    Input: nums = [1, 2, 3, 4]
    Output: -1
    Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Note:  
-   nums will have a length in the range [1, 50].
-   Every nums[i] will be an integer in the range [0, 99].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/largest-number-at-least-twice-of-others)  

Credits To: [leetcode.com](https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/largest-number-at-least-twice-of-others
    ## Basic Ideas: Find the largest element and the second largest element
    ##              Check whether: the largest is at least twice as much as the second largest element
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def dominantIndex(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length == 0:
                return -1
            if length == 1:
                return 0
    
            max_index = -1
            for index in xrange(length):
                if max_index == -1:
                    max_index = index
                else:
                    if nums[index] > nums[max_index]:
                        max_index = index
    
            second_max_index = -1
            for index in xrange(length):
                if index == max_index:
                    continue
    
                if second_max_index == -1:
                    second_max_index = index
                else:
                    if nums[index] > nums[second_max_index]:
                        second_max_index = index
    
            if nums[max_index] >= 2* nums[second_max_index]:
                return max_index
            else:
                return -1
    s = Solution()
    print s.dominantIndex([3, 6, 1, 0]) 
    print s.dominantIndex([1, 2, 3, 4])
    print s.dominantIndex([])
    print s.dominantIndex([1])