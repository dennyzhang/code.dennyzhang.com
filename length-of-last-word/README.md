# Leetcode: Length of Last Word     :BLOG:Basic:


---

Length of Last Word  

---

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.  

If the last word does not exist, return 0.  

Note: A word is defined as a character sequence consists of non-space characters only.  

    Example:
    
    Input: "Hello World"
    Output: 5

Blog link: <http://brain.dennyzhang.com/length-of-last-word>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/length-of-last-word)  

Credits To: [leetcode.com](https://leetcode.com/problems/length-of-last-word/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def lengthOfLastWord(self, s):
            """
            :type s: str
            :rtype: int
            """
            s = s.strip(" ")
            word_list = s.split(" ")
            return len(word_list[-1])