
# Leetcode: Swap Adjacent in LR String     :BLOG:Medium:

---

Swap Adjacent in LR String  

---

Similar Problems:  

-   [Valid Parenthesis String](https://code.dennyzhang.com/valid-parenthesis-string)
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   Tag: [math](https://code.dennyzhang.com/tag/math)

---

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.  

Example:  

    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Output: True
    Explanation:
    We can transform start to end following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX

Note:  

1.  1 <= len(start) = len(end) <= 10000.
2.  Both start and end will only consist of characters in {'L', 'R', 'X'}.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/swap-adjacent-in-lr-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/swap-adjacent-in-lr-string/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/swap-adjacent-in-lr-string
    ## Basic Ideas: Check 3 rules
    ##       R won't bypass X: count 'R' from left to right
    ##       X won't bypass L: count 'L' from right to left 
    ##       R won't bypass L: remove 'X', then confirm two strings equal
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def canTransform(self, start, end):
    	"""
    	:type start: str
    	:type end: str
    	:rtype: bool
    	"""
    	if start.count('X') != end.count('X') or \
    	    start.count('L') != end.count('L') or \
    	    start.count('R') != end.count('R'):
    		return False
    
    	## Pass1: from left to right, 'R' count in start should be no smaller than end string
    	count1, count2 = 0, 0
    	for i in range(0, len(start)):
    	    if start[i] == 'R': count1 += 1
    	    if end[i] == 'R': count2 += 1
    	    if count1<count2: return False
    
    	## Pass2: from right to left, 'L' count in start should be no smaller than end string
    	count1, count2 = 0, 0
    	for i in range(len(start)-1, -1, -1):
    	    if start[i] == 'L': count1 += 1
    	    if end[i] == 'L': count2 += 1
    	    if count1<count2: return False
    
    	# check3: remove X, then the two shall equal
    	return start.replace('X', '') == end.replace('X', '')

