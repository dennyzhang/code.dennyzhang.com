
# Leetcode: Permutation in String     :BLOG:Medium:

---

Permutation in String  

---

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.  

    Example 1:
    Input:s1 = "ab" s2 = "eidbaooo"
    Output:True
    Explanation: s2 contains one permutation of s1 ("ba").

    Example 2:
    Input:s1= "ab" s2 = "eidboaoo"
    Output: False

Note:  

1.  The input strings only contain lower case letters.
2.  The length of both given strings is in range [1, 10,000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/permutation-in-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/permutation-in-string/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/permutation-in-string
    ## Basic Ideas: Sliding window in s2 with length of s1
    ##              It has only lowercase, use ch[26] to speed up the comparision.
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def checkInclusion(self, s1, s2):
    	"""
    	:type s1: str
    	:type s2: str
    	:rtype: bool
    	"""
    	len1, len2 = len(s1), len(s2)
    	if len1>len2: return False
    	list1, list2 = [0]*26, [0]*26
    	for i in range(0, len1):
    	    list1[ord(s1[i]) - ord('a')] += 1
    	    list2[ord(s2[i]) - ord('a')] += 1
    	if list1 == list2: return True
    	for i in range(len1, len2):
    	    # slide window
    	    list2[ord(s2[i]) - ord('a')] += 1
    	    list2[ord(s2[i-len1]) - ord('a')] -= 1
    	    if list1 == list2: return True            
    
    	return False

