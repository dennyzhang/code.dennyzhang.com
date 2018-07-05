
# Leetcode: Longest Consecutive Sequence     :BLOG:Hard:

---

Longest Consecutive Sequence  

---

Similar Problems:  

-   Tag: [#subarray](https://code.dennyzhang.com/tag/subarray)

---

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.  

For example,  
Given [100, 4, 200, 1, 3, 2],  
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.  

Your algorithm should run in O(n) complexity.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/longest-consecutive-sequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-consecutive-sequence/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/longest-consecutive-sequence
    class Solution:
        # Compared to longestConsecutive_v1, no need to search in both directions.
        def longestConsecutive(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: int
    	"""
    	if len(nums) == 0: return 0
    	s = set(nums)
    	max_count = 0
    	for num in set(nums):
    	    # only search from the biggest value of current group
    	    if num + 1 not in nums:
    		y = num - 1
    		while y in nums:
    		    y = y -1
    		max_count = max(max_count, num-y)
    	return max_count
    
        ## Basic Ideas: one consecutive sequence will be one group
        ##       Build a hashmap
        ##       Then loop, combine group, and delete the absorted elements
        ##
        ##  Clarifications: Does the list contains duplicate elements? 
        ##           If yes, how you would like to treat the duplicate?
        ##
        ## Complexity: Time O(n), Space O(n)
        def longestConsecutive_v1(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: int
    	"""
    	if len(nums) == 0: return 0
    	s = set(nums)
    	max_count = 0
    	while len(s) != 0:
    	    num = s.pop()
    	    count = 1
    	    # search bigger values
    	    v = num
    	    while v+1 in s:
    		count += 1
    		v += 1
    		s.remove(v)
    	    # search smaller values
    	    v = num
    	    while v-1 in s:
    		count += 1
    		v -= 1
    		s.remove(v)
    	    max_count = max(max_count, count)
    	return max_count

