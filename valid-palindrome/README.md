# Leetcode: Valid Palindrome     :BLOG:Basic:


---

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  

---

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  

For example,  
"A man, a plan, a canal: Panama" is a palindrome.  
"race a car" is not a palindrome.  

Note:  
Have you consider that the string might be empty? This is a good question to ask during an interview.  

For the purpose of this problem, we define empty string as valid palindrome.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-palindrome)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-palindrome/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/valid-palindrome
    class Solution(object):
        def isPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            if s == "":
                return True
            washed_string = []
            for ch in s:
                if (ch >='a' and ch <='z') or (ch >='A' and ch <='Z') or (ch >='0' and ch <='9'):
                    washed_string.append(ch.lower())
            # print("washed_string: %s, target: %s" % (washed_string, washed_string[::-1]))
            return washed_string == washed_string[::-1]