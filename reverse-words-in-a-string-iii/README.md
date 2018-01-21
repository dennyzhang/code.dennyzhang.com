# Leetcode: Reverse Words in a String III     :BLOG:Basic:


---

Reverse Words in a String III  

---

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.  

Example 1:  
Input: "Let's take LeetCode contest"  
Output: "s'teL ekat edoCteeL tsetnoc"  
Note: In the string, each word is separated by single space and there will not be any extra space in the string.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-words-in-a-string-iii)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-words-in-a-string-iii/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def reverseWords(self, s):
            """
            :type s: str
            :rtype: str
            """
            reversed_word_list = []
            for word in s.split(" "):
                reversed_word_list.append(word[::-1])
    
            return " ".join(reversed_word_list)