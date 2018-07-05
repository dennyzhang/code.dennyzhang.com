
# Leetcode: Sort Characters By Frequency     :BLOG:Basic:

---

Sort Characters By Frequency  

---

Similar Problems:  

-   [Review: Heap Problems](https://code.dennyzhang.com/review-heap), [Tag: #heap](https://code.dennyzhang.com/tag/heap)
-   Tag: [heap](https://code.dennyzhang.com/tag/heap)

---

Given a string, sort it in decreasing order based on the frequency of characters.  

Example 1:  

    Input:
    "tree"
    
    Output:
    "eert"
    
    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:  

    Input:
    "cccaaa"
    
    Output:
    "cccaaa"
    
    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:  

    Input:
    "Aabb"
    
    Output:
    "bbAa"
    
    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/sort-characters-by-frequency)  

Credits To: [leetcode.com](https://leetcode.com/problems/sort-characters-by-frequency/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/sort-characters-by-frequency
    ## Baisc Ideas: Sort with customized function
    ##
    ## Complexity:
    import collections
    class Solution(object):
        def frequencySort(self, s):
    	"""
    	:type s: str
    	:rtype: str
    	"""
    	m = collections.defaultdict(lambda: 0)
    	for ch in s: m[ch] += 1
    	def myCompare(v1, v2):
    	    if m[v1] > m[v2]: return -1
    	    elif m[v1] < m[v2]: return 1
    	    else:
    		if v1 == v2: return 0
    		return -1 if v1 < v2 else 1
    	return ''.join(sorted(s, cmp=myCompare))
    
    # s = Solution()
    # print s.frequencySort("Aabb") # "bbAa"

