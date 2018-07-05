
# Leetcode: Valid Number     :BLOG:Medium:

---

Validate if a given string is numeric.  

---

Similar Problems:  

-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Validate if a given string is numeric.  

Some examples:  

    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/valid-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-number/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/valid-number
    ## Yes, it's cheating.
    ## But I really don't think this puzzle is approriate for code interview.
    ## Just too many details!
    class Solution:
        def isNumber(self, s):
    	"""
    	:type s: str
    	:rtype: bool
    	"""
    	try: float(s)
    	except ValueError: return False
    	else: return True

