# Leetcode: Repeated DNA Sequences     :BLOG:Basic:


---

Repeated DNA Sequences  

---

Similar Problems:  
-   [Review: String Problems](https://code.dennyzhang.com/review-string), Tag: [#string](https://code.dennyzhang.com/tag/string)

---

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.  

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.  

For example,  

    Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
    
    Return:
    ["AAAAACCCCC", "CCCCCAAAAA"].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/repeated-dna-sequences)  

Credits To: [leetcode.com](https://leetcode.com/problems/repeated-dna-sequences/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/repeated-dna-sequences
    ## Basic Ideas: sliding window + hashmap
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def findRepeatedDnaSequences(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            length = len(s)
            if length <= 10: return []
            import collections
            d = collections.defaultdict(lambda:0)
            curStr = s[0:10]
            d[curStr] += 1
            res = []
            for i in range(10, length):
                curStr = curStr[1:] + s[i]
                if d[curStr] == 1: res.append(curStr)
                d[curStr] += 1
            return res