# Leetcode: Custom Sort String     :BLOG:Basic:


---

Custom Sort String  

---

Similar Problems:  
-   [Review: String Problems](https://brain.dennyzhang.com/review-string), Tag: [#string](https://brain.dennyzhang.com/tag/string)

---

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.  

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.  

Return any permutation of T (as a string) that satisfies this property.  

Example :  

    Input: 
    S = "cba"
    T = "abcd"
    Output: "cbad"
    Explanation: 
    "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
    Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:  

-   S has length at most 26, and no character is repeated in S.
-   T has length at most 200.
-   S and T consist of lowercase letters only.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/custom-sort-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/custom-sort-string/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/custom-sort-string
    ## Basic Ideas: hashmap
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def customSortString(self, S, T):
            """
            :type S: str
            :type T: str
            :rtype: str
            """
            import collections
            d = collections.defaultdict(lambda: 0)
            for ch in T: d[ch] += 1
    
            res = ""
            for ch in S:
                if ch in d:
                    res = "%s%s" % (res, ch*d[ch])
                    d[ch] = 0
    
            for ch in d:
                if d[ch] != 0:
                    res = "%s%s" % (res, ch*d[ch])
            return res