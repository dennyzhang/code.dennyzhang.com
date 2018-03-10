# Lintcode: String Replace     :BLOG:Hard:


---

String Replace  

---

Similar Problems:  
-   [Tag: #string](https://brain.dennyzhang.com/tag/string)

---

Given two identical-sized string array A, B and a string S. All substrings A appearing in S are replaced by B.(Notice: From left to right, it must be replaced if it can be replaced. If there are multiple alternatives, replace longer priorities. After the replacement of the characters can't be replaced again.)  

Notice  
-   The size of each string array does not exceed 100, the total string length does not exceed 50000.
-   The lengths of A [i] and B [i] are equal.
-   The length of S does not exceed 50000.
-   All characters are lowercase letters.
-   We guarantee that the A array does not have the same string

Example  
Given A = ["ab","aba"], B = ["cc","ccc"], S = "ababa", return "cccba".  

    In accordance with the rules, the substring that can be replaced is "ab" or "aba". Since "aba" is longer, we replace "aba" with "ccc".

Given A = ["ab","aba"], B = ["cc","ccc"] ,S = "aaaaa" ,return "aaaaa".  

    S does not contain strings in A, so no replacement is done.

Given A = ["cd","dab","ab"], B = ["cc","aaa","dd"], S = "cdab", return "ccdd".  

    From left to right, you can find the "cd" can be replaced at first, so after the replacement becomes "ccab", then you can find "ab" can be replaced, so the string after the replacement is "ccdd".

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/string-replace)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/string-replace/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/string-replace
    class TrieNode:
        def __init__(self):
            import collections
            self.value = None
            self.children = collections.defaultdict(TrieNode)
    
    class Solution:
        """
        @param a: The A array
        @param b: The B array
        @param s: The S string
        @return: The answer
        """
        def stringReplace(self, a, b, s):
            ## Basic Ideas: Trie tree
            ## Complexity: Time O(kn), Space O(m)
            ##      n = len(s), m = total string length of a
            root = TrieNode()
    
            # add node to TrieTree
            for i in range(len(a)):
                string = a[i]
                if string not in s: continue
                p = root
                for ch in string:
                    p = p.children[ch]
                p.value = b[i]
    
            # search TrieTree
            res = ""
            i = 0
            while i<len(s):
                p = root
                index, string = i, None
                for j in range(i, len(s)):
                    ch = s[j]
                    if ch not in p.children:
                        break
                    p = p.children[ch]
                    # track possible result
                    if p.value:
                        index, string = j, p.value
    
                if string is not None:
                    res += string
                    i = index + 1
                else:
                    res += s[i]
                    i += 1
    
            # get the result
            return res