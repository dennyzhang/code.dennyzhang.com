# Leetcode: Longest Word in Dictionary through Deleting     :BLOG:Medium:


---

Longest Word in Dictionary through Deleting  

---

Similar Problems:  
-   [Review: String Problems](https://brain.dennyzhang.com/review-string), Tag: [#string](https://brain.dennyzhang.com/tag/string)

---

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.  

Example 1:  

    Input:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    
    Output: 
    "apple"

Example 2:  

    Input:
    s = "abpcplea", d = ["a","b","c"]
    
    Output: 
    "a"

Note:  
1.  All the strings in the input will only contain lower-case letters.
2.  The size of the dictionary won't exceed 1,000.
3.  The length of all the strings in the input won't exceed 1,000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-word-in-dictionary-through-deleting)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/longest-word-in-dictionary-through-deleting
    ## Basic Ideas: sort, then two pointers
    ##
    ## Complexity: Time O(n*log(n)), Space O(1)
    class Solution:
        def findLongestWord(self, s, d):
            """
            :type s: str
            :type d: List[str]
            :rtype: str
            """
            d.sort(key=lambda x: (-len(x), x))
            for word in d:
                i = 0
                # loop s
                for ch in s:
                    if i == len(word): break
                    if ch == word[i]: i+= 1
                if i == len(word): return word
            return ''