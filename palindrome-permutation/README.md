# Leetcode: Palindrome Permutation     :BLOG:Medium:


---

Palindrome Permutation  

---

Similar Problems:  
-   [Review: Palindrome Problems](https://brain.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://brain.dennyzhang.com/tag/palindrome)

---

Given a string, determine if a permutation of the string could form a palindrome.  

For example,  
"code" -> False, "aab" -> True, "carerac" -> True.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/palindrome-permutation)  

Credits To: [leetcode.com](https://leetcode.com/problems/palindrome-permutation/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/palindrome-permutation
    ## Basic Ideas: set. With one pass
    ##
    ## Complexity: Time O(n), Space O(1)
    ##             The character is a limited set, thus the space is O(1)
    class Solution:
        def canPermutePalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            myset = set([])
            for ch in s:
                if ch in myset:
                    myset.remove(ch)
                else:
                    myset.add(ch)
            return len(myset) <= 1