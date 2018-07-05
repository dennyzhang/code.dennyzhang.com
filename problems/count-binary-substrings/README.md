
# Leetcode: Count Binary Substrings     :BLOG:Amusing:

---

Count Binary Substrings  

---

Similar Problems:  

-   [Review: TwoPointers Problems](https://code.dennyzhang.com/review-twopointer)
-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.  

Substrings that occur multiple times are counted the number of times they occur.  

    Example 1:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    
    Notice that some of these substrings repeat and are counted the number of times they occur.
    
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

    Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
    Note:
    
    s.length will be between 1 and 50,000.
    s will only consist of "0" or "1" characters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/count-binary-substrings)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-binary-substrings/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/count-binary-substrings
    ## Basic Ideas: Two pointers
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def countBinarySubstrings(self, s):
    	"""
    	:type s: str
    	:rtype: int
    	"""
    	length = len(s)
    	res, g0_cnt, g1_cnt = 0, 0, 0
    	for i in range(0, length):
    	    if s[i] == '0':
    		g0_cnt += 1
    	    else:
    		g1_cnt += 1
    
    	    if i == length -1:
    		res += min(g0_cnt, g1_cnt)
    		continue
    
    	    if s[i] != s[i+1]:
    		res += min(g0_cnt, g1_cnt)
    		# change counter
    		if s[i] == '1':
    		    g0_cnt = 0
    		else:
    		    g1_cnt = 0
    	return res

