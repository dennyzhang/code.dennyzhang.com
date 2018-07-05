
# Leetcode: Reverse String II     :BLOG:Basic:

---

Reverse string  

---

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.  

    Example:
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Restrictions:  

1.  The string consists of lower English letters only.
2.  Length of the given string and k will in the range [1, 10000]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/reverse-string-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-string-ii/description/)  

Hint: Time O(n), Space O(1). Moore voting  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/reverse-string-ii
    ## Basic Ideas:
    ## Complexity: Time O(n), Space O(1)
    ## Assumptions:
    class Solution(object):
        def reverseStr(self, s, k):
    	"""
    	:type s: str
    	:type k: int
    	:rtype: str
    	"""
    	length = len(s)
    	l = list(s)
    	should_reverse = True
    	i = 0
    	while i < length:
    	    if i+k-1 < length:
    		j = i+k-1
    	    else:
    		j = length - 1
    
    	    if should_reverse:
    		# print("i: %d, j: %d" % (i, j))
    		start = i
    		end = j
    		while start < end:
    		    l[start],l[end] = l[end], l[start]
    		    start += 1
    		    end -= 1
    	    should_reverse = not should_reverse
    	    i = j + 1
    	return ''.join(l)

