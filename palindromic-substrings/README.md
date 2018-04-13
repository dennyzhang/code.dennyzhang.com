# Leetcode: Palindromic Substrings     :BLOG:Medium:


---

Palindromic Substrings  

---

Similar Problems:  
-   [Review: Palindrome Problems](https://code.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://code.dennyzhang.com/tag/palindrome)

---

Given a string, your task is to count how many palindromic substrings in this string.  

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.  

Example 1:  

    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:  

    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:  
The input string length won't exceed 1000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/palindromic-substrings)  

Credits To: [leetcode.com](https://leetcode.com/problems/palindromic-substrings/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/palindromic-substrings
    ## Basic Ideas: Choose each character as the central letter
    ##        The palindrome may have odd length and even length.
    ## Complexity: Time O(n*n), Space O(1)
    class Solution:
        def countSubstrings(self, s):
            """
            :type s: str
            :rtype: int
            """
            length = len(s)
            res = length
            for i in range(length):
                for (l,r) in [(i-1, i+1), (i, i+1)]:
                    while l >=0 and r <= length-1 and s[l] == s[r]:
                        res += 1
                        l, r = l-1, r+1
            return res