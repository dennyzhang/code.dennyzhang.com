
# Leetcode: Rotated Digits     :BLOG:Basic:

---

Rotated Digits  

---

Similar Problems:  

-   [Review: String Problems](https://code.dennyzhang.com/review-string)
-   Tag: [#string](https://code.dennyzhang.com/tag/string), [#rotateoperation](https://code.dennyzhang.com/tag/rotateoperation)

---

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X. A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number.  

Now given a positive number N, how many numbers X from 1 to N are good?  

Example:  

    Input: 10
    Output: 4
    Explanation: 
    There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:  
N  will be in range [1, 10000].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/rotated-digits)  

Credits To: [leetcode.com](https://leetcode.com/problems/rotated-digits/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/rotated-digits
    ## Basic Ideas: Check number one by one
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def rotatedDigits(self, N):
    	"""
    	:type N: int
    	:rtype: int
    	"""
    	res = 0
    	for num in range(1, N+1):
    	    has_changed, is_valid = False, True
    	    for ch in str(num):
    		if ch in "347":
    		    is_valid = False
    		    break
    		if ch in "2569": has_changed = True
    	    if has_changed and is_valid: res += 1
    	return res

