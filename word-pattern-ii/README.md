# Leetcode: Word Pattern II     :BLOG:Basic:


---

Word Pattern II  

---

Similar Problems:  
-   [Word Pattern](https://code.dennyzhang.com/word-pattern)
-   [Review: String Problems](https://code.dennyzhang.com/review-string), Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Given a pattern and a string str, find if str follows the same pattern.  

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.  

Examples:  
1.  pattern = "abab", str = "redblueredblue" should return true.
2.  pattern = "aaaa", str = "asdasdasdasd" should return true.
3.  pattern = "aabb", str = "xyzabcxzyabc" should return false.

Notes:  
You may assume both pattern and str contains only lowercase letters.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/word-pattern-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/word-pattern-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/word-pattern-ii
    ## Basic Ideas:
    ##  In str, not all words are the same length
    ##
    ## Complexity:
    class Solution(object):
        def wordPatternMatch(self, pattern, str):
            """
            :type pattern: str
            :type str: str
            :rtype: bool
            """
            len1, len2 = len(pattern), len(str)
            if len1 == 0 or len2 == 0: return len1 == len2
            # problematic?
            if len2%len1 != 0: return False
            word_len = len2/len1
            d, seen = {}, set([])
            for i in range(len1):
                ch = pattern[i]
                word = str[i*word_len:(i+1)*word_len]
                if ch in d:
                    if d[ch] != word: return False
                else:
                    if word in seen: return False
                    d[ch] = word
                    seen.add(word)
            return True