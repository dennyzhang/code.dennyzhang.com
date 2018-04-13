# Leetcode: Ransom Note     :BLOG:Basic:


---

Ransom Note  

---

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.  

Each letter in the magazine string can only be used once in your ransom note.  

Note:  
You may assume that both strings contain only lowercase letters.  

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/ransom-note)  

Credits To: [leetcode.com](https://leetcode.com/problems/ransom-note/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/ransom-note
    class Solution(object):
        def canConstruct(self, ransomNote, magazine):
            """
            :type ransomNote: str
            :type magazine: str
            :rtype: bool
            """
            ## Idea: 2 dict
            ## Complexity: Time O(n), Space O(n)
            lower_letters = map(chr, range(ord('a'), ord('z')+1))
            r_dict = {}
            m_dict = {}
            for ch in lower_letters:
                r_dict[ch] = 0
                m_dict[ch] = 0
    
            for ch in ransomNote:
                r_dict[ch] += 1
    
            for ch in magazine:
                m_dict[ch] += 1
    
            for ch in lower_letters:
                if m_dict[ch] - r_dict[ch] < 0:
                    return False
            return True