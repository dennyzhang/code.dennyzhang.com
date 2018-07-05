
# Leetcode: Contains Duplicate III     :BLOG:Medium:

---

Contains Duplicate III  

---

Similar Problems:  

-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/contains-duplicate-iii)  

Credits To: [leetcode.com](https://leetcode.com/problems/contains-duplicate-iii/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/contains-duplicate-iii
    ## Basic Ideas: sliding window
    ##              Maintain a window with k+1 elements. A set for unsorted unique collection
    ## Complexity: Time O(n), Space O(k)
    class Solution(object):
        def containsNearbyAlmostDuplicate(self, nums, k, t):
    	"""
    	:type nums: List[int]
    	:type k: int
    	:type t: int
    	:rtype: bool
    	"""
    	length = len(nums)
    	if length <= 0: return False
    	if k == 0: return False
    	s = set([])
    	for i in xrange(length):
    	    if i > k:
    		s.remove(nums[i-k-1])
    	    for v in s:
    		if abs(nums[i]-v) <= t:
    		    return True
    	    s.add(nums[i])
    	return False
    
    # s = Solution()
    # print s.containsNearbyAlmostDuplicate([-1, -1], 1, 0) # True
    # print s.containsNearbyAlmostDuplicate([-1, -1], 1, 1) # True
    # print s.containsNearbyAlmostDuplicate([99, 99], 1, 1) # True
    # print s.containsNearbyAlmostDuplicate([1, 2, 1], 0, 1) # False
    # print s.containsNearbyAlmostDuplicate([0, 2147483647], 1, 2147483647) # True

