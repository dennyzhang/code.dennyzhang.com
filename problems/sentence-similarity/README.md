# Leetcode: Sentence Similarity     :BLOG:Basic:


---

Sentence Similarity  

---

Similar Problems:  
-   [Replace Words](https://code.dennyzhang.com/replace-words)
-   [Tag: #hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.  

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].  

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.  

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.  

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.  

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].  

Note:  

-   The length of words1 and words2 will not exceed 1000.
-   The length of pairs will not exceed 2000.
-   The length of each pairs[i] will be 2.
-   The length of each words[i] and pairs[i][j] will be in the range [1, 20].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sentence-similarity)  

Credits To: [leetcode.com](https://leetcode.com/problems/sentence-similarity/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/sentence-similarity
    ## Basic Ideas: hashmap
    ##
    ## Assumption: paris are valid
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def areSentencesSimilar(self, words1, words2, pairs):
            """
            :type words1: List[str]
            :type words2: List[str]
            :type pairs: List[List[str]]
            :rtype: bool
            """
            if len(words1) != len(words2): return False
    
            # build hashmap
            d = collections.defaultdict(set)
            for [string1, string2] in pairs:
                d[string1].add(string2)
                d[string2].add(string1)
    
            # check word by word
            for i in range(len(words1)):
                word1, word2 = words1[i], words2[i]
                if word1 == word2: continue
                if word2 not in d[word1]: return False
            return True