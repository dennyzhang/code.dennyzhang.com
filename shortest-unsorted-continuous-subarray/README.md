# Leetcode: Shortest Unsorted Continuous Subarray     :BLOG:Amusing:


---

Shortest Unsorted Continuous Subarray  

---

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.  

You need to find the shortest such subarray and output its length.  

    Example 1:
    Input: [2, 6, 4, 8, 10, 9, 15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
    Note:
    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/shortest-unsorted-continuous-subarray)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/shortest-unsorted-continuous-subarray
    ## Basic Ideas: If the first element is not the minimum, the subarray must starts with the first position
    ##              If the last element is not the maxmimum, the subarray must ends with the last position
    ##
    ##              Copy the list and sort it.
    ##              Check from head of both array, if the same, keep going right. Otherwise we found the start position
    ##              Check from the tail of both array, if the same, keep going left. Otherwise we found the end position
    ##              end position shouldn't pass the start position
    ##
    ## Complexity: Time O(n*log(n)), Space O(n)
    class Solution(object):
        def findUnsortedSubarray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length <= 1: return 0
            nums2 = sorted(nums)
    
            start = 0
            while start < length and nums[start] == nums2[start]:
                start += 1
    
            # If already sorted, start would be length
            if start == length: return 0
    
            end = length-1
            while end > start and end > 0 and nums[end] == nums2[end]:
                end -= 1
    
            return end - start + 1