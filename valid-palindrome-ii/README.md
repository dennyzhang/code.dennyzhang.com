# Leetcode: Valid Palindrome II     :BLOG:Medium:


---

Valid Palindrome II  

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

Blog link: <http://brain.dennyzhang.com/valid-palindrome-ii>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas:
    ##      Two pointers: one from left to right, another from right to left
    ##      If the value is different, we could either delete the left one or delete the right one
    ##      Then the remaining should be a Palindrome
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def validPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            start, end = 0, len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    if self.isPalindrome(s, start+1, end):
                        # delete the left
                        return True
                    else:
                        return self.isPalindrome(s, start, end-1)
                start += 1
                end -= 1
            return True
    
        def isPalindrome(self, s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True