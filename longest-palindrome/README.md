# Leetcode: Longest Palindrome     :BLOG:Basic:


---

Longest Palindrome  

---

Similar Problems:  
-   [Review: Palindrome Problems](https://code.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://code.dennyzhang.com/tag/palindrome)

---

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.  

This is case sensitive, for example "Aa" is not considered a palindrome here.  

Note:  
Assume the length of given string will not exceed 1,010.  

    Example:
    
    Input:
    "abccccdd"
    
    Output:
    7
    
    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-palindrome)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-palindrome/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/longest-palindrome
    ## Basic Ideas:
    ## Complexity:
    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: int
            """
            ## Idea: Use a map and count characters
            ## Complexity:
            count_map = {}
            for ch in s:
                if count_map.has_key(ch) is False:
                    count_map[ch] = 1
                else:
                    count_map[ch] += 1
            has_odd = False
            res = 0
            for ch in count_map.keys():
                if count_map[ch] % 2 == 0:
                    res += count_map[ch]
                else:
                    has_odd = True
                    res += count_map[ch] - 1
            return res+1 if has_odd else res