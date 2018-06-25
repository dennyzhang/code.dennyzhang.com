
# Leetcode: Missing Ranges     :BLOG:Basic:

---

Missing Ranges  

---

Similar Problems:  

-   [Meeting Rooms](https://code.dennyzhang.com/meeting-rooms)
-   [Review: Interval Problems](https://code.dennyzhang.com/review-interval), [Tag: #interval](https://code.dennyzhang.com/tag/interval)

---

Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.  

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/missing-ranges)  

Credits To: [leetcode.com](https://leetcode.com/problems/missing-ranges/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/missing-ranges
    ## Basic Ideas:
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def findMissingRanges(self, nums, lower, upper):
    	"""
    	:type nums: List[int]
    	:type lower: int
    	:type upper: int
    	:rtype: List[str]
    	"""
    	l = []
    	target = lower
    	for num in nums:
    	    if num > target:
    		if num == target + 1:
    		    l.append(str(target))
    		else:
    		    l.append("%s->%s" % (target, num-1))
    	    target = num + 1
    
    	if target <= upper:
    	    if target == upper:
    		l.append(str(target))
    	    else:
    		l.append("%s->%s" % (target, upper))
    	return l

