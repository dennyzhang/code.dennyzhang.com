# Leetcode: Valid Palindrome     :BLOG:Basic:


---

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  

---

Similar Problems:  
-   [Review: Palindrome Problems](https://brain.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://brain.dennyzhang.com/tag/palindrome)
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://brain.dennyzhang.com/tag/twopointer)

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

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/valid-palindrome
    ## Basic Ideas: two pointer
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def isPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            length = len(s)
            if length == 0: return True
            left, right = 0, length-1
            while left<right:
                if not s[left].isalnum():
                    left += 1
                    continue
                if not s[right].isalnum():
                    right -= 1
                    continue
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left+1, right-1
            return True
    
    s = Solution()
    print(s.isPalindrome("aa"))