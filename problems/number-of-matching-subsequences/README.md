# Leetcode: Number of Matching Subsequences     :BLOG:Medium:


---

Number of Matching Subsequences  

---

Similar Problems:  
-   [Tag: #subsequence](https://code.dennyzhang.com/tag/subsequence)

---

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.  

Example :  

    Input: 
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    Output: 3
    Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:  

-   All words in words and S will only consists of lowercase letters.
-   The length of S will be in the range of [1, 50000].
-   The length of words will be in the range of [1, 5000].
-   The length of words[i] will be in the range of [1, 50].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-matching-subsequences)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-matching-subsequences/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/number-of-matching-subsequences
    ## Basic Ideas:
    ## Complexity: Time O(n*m), Space O(1)
    class Solution:
        def numMatchingSubseq(self, S, words):
            """
            :type S: str
            :type words: List[str]
            :rtype: int
            """
            res = 0
            ok_set = set([])
            invalid_set = set([])
            for word in words:
                # avoid duplicate calculation
                if word in ok_set:
                    res += 1
                    continue
    
                if word in invalid_set: continue
    
                index = 0
                for ch in S:
                    if ch == word[index]: index += 1
                    if index == len(word):
                        res += 1
                        break
    
                if index != len(word):
                    invalid_set.add(word)
                else:
                    ok_set.add(word)
            return res