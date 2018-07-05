
# Leetcode: Isomorphic Strings     :BLOG:Basic:

---

Isomorphic Strings  

---

Given two strings s and t, determine if they are isomorphic.  

Two strings are isomorphic if the characters in s can be replaced to get t.  

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.  

    For example,
    Given "egg", "add", return true.
    
    Given "foo", "bar", return false.
    
    Given "paper", "title", return true.

Note:  
You may assume both s and t have the same length.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/isomorphic-strings)  

Credits To: [leetcode.com](https://leetcode.com/problems/isomorphic-strings/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/isomorphic-strings
    ## Basic Ideas:
    ##             Build 2 dicts
    ##             From s to t, and from t to s
    ##             For any new item to compare, make sure it won't viloate any dict
    ## Complexity: Time O(n), Space O(1). (Keys of dictionary is quite limited)
    class Solution(object):
        def isIsomorphic(self, s, t):
    	"""
    	:type s: str
    	:type t: str
    	:rtype: bool
    	"""
    	m1, m2 = {}, {}
    	for i in xrange(len(s)):
    	    ch1, ch2 = s[i], t[i]
    	    # mapping from s to t
    	    if m1.has_key(ch1):
    		if m1[ch1] != ch2:
    		    return False
    	    else:
    		m1[ch1] = ch2
    
    	    # ab -> aa
    	    # mapping from t to s
    	    if m2.has_key(ch2):
    		if m2[ch2] != ch1:
    		    return False
    	    else:
    		m2[ch2] = ch1
    	return True

