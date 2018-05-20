# Leetcode: Letter Case Permutation     :BLOG:Basic:


---

Letter Case Permutation  

---

Similar Problems:  
-   [Generalized Abbreviation](https://code.dennyzhang.com/generalized-abbreviation)
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination), [Tag: #combination](https://code.dennyzhang.com/tag/combination)
-   [Review: Recursive Problems](https://code.dennyzhang.com/review-recursive), [Tag: #recursive](https://code.dennyzhang.com/tag/recursive)

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

---

    ## Blog link: https://code.dennyzhang.com/letter-case-permutation
    class Solution:
        ## Basic Ideas: One pass (similar like DFS)
        ##
        ## Complexity: Time O(n*pow(2,n)), Space O(pow(2, n))
        def letterCasePermutation(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            res = [""]
            for ch in S:
                l = []
                for item in res:
                    if ch.isdigit():
                        l.append("%s%s" % (item, ch))
                    else:
                        l.append("%s%s" % (item, ch.lower()))
                        l.append("%s%s" % (item, ch.upper()))
                res = l
            return res
    
        ## Basic Ideas: BFS
        ##
        ## Complexity: Time O(n*pow(2, n)), Space O(pow(2, n))
        def letterCasePermutation_v1(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            length = len(S)
            if length == 0: return [""]
            import collections
            queue = collections.deque()
            queue.append("")
            level = -1
            while True:
                level += 1
                if level == length: break
                for k in range(len(queue)):
                    ch = S[level]
                    element = queue.popleft()
                    if ch.isdigit():
                        queue.append("%s%s" % (element, ch))
                    else:
                        queue.append("%s%s" % (element, ch.lower()))
                        queue.append("%s%s" % (element, ch.upper()))
            return list(queue)
    
        ## Basic Ideas: recursive
        ##
        ## Complexity: Time O(n*pow(2, n)), Space O(pow(2, n))
        def letterCasePermutation_v1(self, S):
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