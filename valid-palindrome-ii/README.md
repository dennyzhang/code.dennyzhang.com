# Leetcode: Valid Palindrome II     :BLOG:Medium:


---

Valid Palindrome II  

---

Similar Problems:  
-   [Review: Palindrome Problems](https://brain.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://brain.dennyzhang.com/tag/palindrome)

---

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.  

    Example 1:
    Input: "aba"
    Output: True

    Example 2:
    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

Note:  
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-palindrome-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-palindrome-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/valid-palindrome-ii
    ## Basic Ideas: If mismatched, we can only delete either the left or the right
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def validPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            if self.isPalindrome(s): return True
            l, r = 0, len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    # keep right
                    if self.isPalindrome(s[l+1:r+1]): return True
                    # keep left
                    if self.isPalindrome(s[l:r]): return True
                    return False
                l,r = l+1, r-1
            return True
    
        def isPalindrome(self, s):
            length = len(s)
            if length == 0: return True
            l, r = 0, length-1
            while l<r:
                if s[l]!=s[r]: return False
                l, r = l+1, r-1
            return True