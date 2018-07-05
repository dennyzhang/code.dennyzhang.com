
# Leetcode: Most Common Word     :BLOG:Basic:

---

Most Common Word  

---

Similar Problems:  

-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.  

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.  

Example:  

    Input: 
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    Output: "ball"
    Explanation: 
    "hit" occurs 3 times, but it is a banned word.
    "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
    Note that words in the paragraph are not case sensitive,
    that punctuation is ignored (even if adjacent to words, such as "ball,"), 
    and that "hit" isn't the answer even though it occurs more because it is banned.

Note:  

-   1 <= paragraph.length <= 1000.
-   1 <= banned.length <= 100.
-   1 <= banned[i].length <= 10.
-   The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
-   paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
-   Different words in paragraph are always separated by a space.
-   There are no hyphens or hyphenated words.
-   Words only consist of letters, never apostrophes or other punctuation symbols.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/most-common-word)  

Credits To: [leetcode.com](https://leetcode.com/problems/most-common-word/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/most-common-word
    ## Basic Ideas: hashmap
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def mostCommonWord(self, paragraph, banned):
    	"""
    	:type paragraph: str
    	:type banned: List[str]
    	:rtype: str
    	"""
    	import collections
    	m = collections.defaultdict(lambda: 0)
    	banned_set = set(banned)
    	paragraph = paragraph.lower()
    
    	max_count = 0
    	word = ""
    	for i, ch in enumerate(paragraph):
    	    if ch.isalpha() is False or i == len(paragraph)-1:
    		if ch.isalpha(): word += ch
    		if word == "": continue
    		if word not in banned_set:
    		    m[word] += 1
    		    max_count = max(max_count, m[word])
    		word = ""
    	    else:
    		word += ch.lower()
    
    	for word in m:
    	    if m[word] == max_count: return word
    	return ""

