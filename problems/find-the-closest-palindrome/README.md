
# Leetcode: Find the Closest Palindrome     :BLOG:Hard:

---

Find the Closest Palindrome  

---

Similar Problems:  

-   [Review: Palindrome Problems](https://code.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://code.dennyzhang.com/tag/palindrome)

---

Given an integer n, find the closest integer (not including itself), which is a palindrome.  

The 'closest' is defined as absolute difference minimized between two integers.  

    Example 1:
    Input: "123"
    Output: "121"

Note:  

1.  The input n is a positive integer represented by string, whose length will not exceed 18.
2.  If there is a tie, return the smaller one as answer.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/find-the-closest-palindrome)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-the-closest-palindrome/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/find-the-closest-palindrome
    ## Basic Ideas: Greedy. Try our best to keep the high digits
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def nearestPalindromic(self, n):
    	"""
    	:type n: str
    	:rtype: str
    	"""
    	length = len(n)
    	if length == 1: return str(int(n)-1)
    
    	k = int(length/2)
    	first_half = n[0:k]
    	# why this?
    	# 10 -> 9
    	if length%2 == 1:
    	    n2="%s%s%s" % (first_half, n[k], first_half[::-1])
    	else:
    	    n2="%s%s" % (first_half, first_half[::-1])
    
    	if n!= n2: return n2
    
    	if length%2==1:
    	    # 20202 -> 20102
    	    if n[k+1] == '0': ch = '1'
    	    else: ch = str(int(n[k])-1)
    	    return "%s%s%s" % (first_half, ch, first_half[::-1])
    	else:
    	    if n[k] == '0': ch = '1'
    	    else: ch = str(int(n[k-1])-1)
    	    res = "%s%s%s%s" % (first_half[:-1], ch, ch, first_half[:-1][::-1])
    	    ## 11 -> 00 -> 0
    	    return str(int(res))

