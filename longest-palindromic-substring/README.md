# Leetcode: Longest Palindromic Substring     :BLOG:Basic:


---

Longest Palindromic Substring  

---

Similar Problems:  
-   [Review: Palindrome Problems](https://code.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://code.dennyzhang.com/tag/palindrome)
-   Tag: [#basic](https://code.dennyzhang.com/category/basic)

---

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.  

Example:  

    Input: "babad"
    
    Output: "bab"
    
    Note: "aba" is also a valid answer.

Example:  

    Input: "cbbd"
    
    Output: "bb"

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-palindromic-substring)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-palindromic-substring/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/longest-palindromic-substring
    ## Basic Ideas: Choose one as the middle of palindromic, then expand in both directions
    ##              palindromic may have odd elements or even elements
    ##
    ## Complexity: Time O(n*n), Space O(1)
    class Solution:
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            length = len(s)
            if length <= 1: return s
            maxCnt, middle = 0, -1
            # check the odd
            for i in range(0, length):
                cnt, j = 1, 1
                while i-j>=0 and i+j<=length-1:
                    if s[i-j] != s[i+j]: break
                    cnt += 2
                    j += 1
                if cnt > maxCnt: maxCnt, middle = cnt, i
    
            # check the even
            for i in range(0, length-1):
                if s[i] != s[i+1]: continue
                cnt, j = 2, 1
                while i-j>=0 and i+j+1<=length-1:
                    if s[i-j] != s[i+j+1]: break
                    cnt += 2
                    j += 1
                if cnt > maxCnt: maxCnt, middle = cnt, i
    
            if maxCnt %2 == 1:
                start = middle - int((maxCnt-1)/2)
            else:
                start = middle - int((maxCnt-2)/2)
            # print(maxCnt, start)
            return s[start:start+maxCnt]