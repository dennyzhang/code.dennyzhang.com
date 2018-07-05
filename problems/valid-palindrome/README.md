
# Leetcode: Valid Palindrome     :BLOG:Basic:

---

Valid Palindrome  

---

Similar Problems:  

-   [Review: Palindrome Problems](https://code.dennyzhang.com/review-palindrome)
-   [Review: TwoPointers Problems](https://code.dennyzhang.com/review-twopointer)
-   Tag: [#palindrome](https://code.dennyzhang.com/tag/palindrome), [#twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  

Note: For the purpose of this problem, we define empty string as valid palindrome.  

Example 1:  

    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:  

    Input: "race a car"
    Output: false

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/valid-palindrome)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-palindrome/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/valid-palindrome
    ## Basic Ideas: two pointer
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def isPalindrome(self, s):
    	"""
    	:type s: str
    	:rtype: bool
    	"""
    	length = len(s)
    	if length == 0: return True
    	left, right = 0, length-1
    	while left<right:
    	    if not s[left].isalnum():
    		left += 1
    		continue
    	    if not s[right].isalnum():
    		right -= 1
    		continue
    	    if s[left].lower() != s[right].lower():
    		return False
    	    left, right = left+1, right-1
    	return True

