# Leetcode: Valid Anagram     :BLOG:Basic:


---

Given two strings s and t, write a function to determine if t is an anagram of s.  

---

Given two strings s and t, write a function to determine if t is an anagram of s.  

    For example,
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.

Note:  
You may assume the string contains only lowercase alphabets.  

Follow up:  
What if the inputs contain unicode characters? How would you adapt your solution to such case?  

Blog link: <http://brain.dennyzhang.com/valid-anagram>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-anagram)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-anagram/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def isAnagram(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            ##Idea: use a dictionary
            ##Complexity: Time O(n), Space O(1)
            count_dict = {}
            for ch in s:
                if count_dict.has_key(ch):
                    count_dict[ch] +=1
                else:
                    count_dict[ch] = 1
    
            for ch in t:
                if count_dict.has_key(ch) is False:
                    return False
                else:
                    count_dict[ch] -= 1
    
            for ch in count_dict.keys():
                if count_dict[ch] != 0:
                    return False
            return True