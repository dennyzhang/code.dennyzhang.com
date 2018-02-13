# Leetcode: One Edit Distance     :BLOG:Medium:


---

One Edit Distance  

---

Similar Problems:  
-   [Edit Distance](https://brain.dennyzhang.com/edit-distance)
-   Tag: [#classic](https://brain.dennyzhang.com/tag/classic)

---

Given two strings S and T, determine if they are both one edit distance apart.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/one-edit-distance)  

Credits To: [leetcode.com](https://leetcode.com/problems/one-edit-distance/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/one-edit-distance
    ## Basic Ideas:
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def isOneEditDistance(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            len_s, len_t = len(s), len(t)
            if abs(len_s - len_t) >= 2: return False
            if len_s == len_t:
                count = 0
                for i in range(len_s):
                    if s[i] != t[i]: count += 1
                    if count > 1: return False
                return count == 1
            else:
                # Use recursive to simplify the logic
                if len_s<len_t: return self.isOneEditDistance(t, s)
                # s is longer
                offset = 0
                for i in range(len_t):
                    if s[i+offset] != t[i]:
                        if offset == 1: return False
                        offset = 1
                        # catch up check
                        if s[i+offset] != t[i]: return False
                return True