# Leetcode: Reverse Vowels of a String     :BLOG:Basic:


---

Reverse Vowels of a String  

---

Write a function that takes a string as input and reverse only the vowels of a string.  

    Example 1:
    Given s = "hello", return "holle".

    Example 2:
    Given s = "leetcode", return "leotcede".

Note:  
The vowels does not include the letter "y".  

Blog link: <http://brain.dennyzhang.com/reverse-vowels-of-a-string>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-vowels-of-a-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-vowels-of-a-string/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def reverseVowels(self, s):
            """
            :type s: str
            :rtype: str
            """
            ## Basic Idea: save vowels in an separated array
            ## Complexity: Time O(n), Space O(n)
            vowel_letters = 'aeiouAEIOU'
            length = len(s)
            vowel_list = []
            for ch in s:
                if ch in vowel_letters:
                    vowel_list.append(ch)
    
            # reverse
            vowel_list = vowel_list[::-1]
    
            ret = [''] * length
    
            k = 0
            for i in range(0, len(s)):
                if s[i] in vowel_letters:
                    ret.append(vowel_list[k])
                    k += 1
                else:
                    ret.append(s[i])
    
            return ''.join(ret)