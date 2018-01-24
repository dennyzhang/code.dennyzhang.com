# Leetcode: Majority Element     :BLOG:Hard:


---

More than half elements are the same. Identify it fast  

---

Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.  

You may assume that the array is non-empty and the majority element always exist in the array.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/majority-element)  

Credits To: [leetcode.com](https://leetcode.com/problems/majority-element/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/majority-element
    class Solution(object):
        def majorityElement1(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ## Ideas: sort, then find the middle item
            ## Complexity: Time O(n*log(n)), Space O(1)
            length = len(nums)
            nums2 = sorted(nums)
            return nums2[(length-1)/2]