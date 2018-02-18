# Leetcode: Letter Case Permutation     :BLOG:Basic:


---

Letter Case Permutation  

---

Similar Problems:  
-   Tag: [#combination](https://brain.dennyzhang.com/tag/combination)

---

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.  

Examples:  

    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: S = "3z4"
    Output: ["3z4", "3Z4"]

    Input: S = "12345"
    Output: ["12345"]

Note:  

-   S will be a string with length at most 12.
-   S will consist only of letters or digits.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/letter-case-permutation)  

Credits To: [leetcode.com](https://leetcode.com/problems/letter-case-permutation/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/letter-case-permutation
    ## Basic Ideas: recursive
    ##
    ## Complexity: Time O(n*pow(2, n)), Space O(pow(2, n))
    class Solution:
        def letterCasePermutation(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            length = len(S)
            if length == 0: return [""]
            res = []
            ch = S[0]
            for item in self.letterCasePermutation(S[1:]):
                if ch.isdigit():
                    res.append("%s%s" % (ch, item))
                else:
                    res.append("%s%s" % (ch.lower(), item))
                    res.append("%s%s" % (ch.upper(), item))
            return res