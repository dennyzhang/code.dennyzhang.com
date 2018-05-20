# Leetcode: Longest Word in Dictionary through Deleting     :BLOG:Medium:


---

Longest Word in Dictionary through Deleting  

---

Similar Problems:  
-   [Interleaving String](https://code.dennyzhang.com/interleaving-string)
-   [Delete Operation for Two Strings](https://code.dennyzhang.com/delete-operation-for-two-strings)
-   [Review: String Problems](https://code.dennyzhang.com/review-string)
-   Tag: [#string](https://code.dennyzhang.com/tag/string)

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

---

    ## Blog link: https://code.dennyzhang.com/longest-word-in-dictionary-through-deleting
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

    // Basic Ideas: Compare s with word one by one
    // Complexity: Time O(n*n), Space O(1)
    func findLongestWord(s string, d []string) string {
        index := -1
        for i, word := range d {
            // check whether s and word can match
            j, has_matched :=0, true
            for _, ch:= range word {
                for j<len(s) && rune(s[j]) != ch { j++ }
                if j==len(s) {
                    has_matched = false
                    break
                }
                j++
            }
            if has_matched == true {
                if index == -1 || len(word)>len(d[index]) {
                    index = i
                }  else {
                    if len(word) == len(d[index]) && word<d[index] {
                        index = i
                    }
                }
            }
        }
        res := ""
        if index != -1 { res = d[index] }
        return res
    }