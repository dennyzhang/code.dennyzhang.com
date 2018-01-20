# Leetcode: First Unique Character in a String     :BLOG:Basic:


---

First Unique Character in a String  

---

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.  

    Examples:
    
    s = "leetcode"
    return 0.
    
    s = "loveleetcode",
    return 2.
    Note: You may assume the string contain only lowercase letters.

Blog link: <http://brain.dennyzhang.com/first-unique-character-in-a-string>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/first-unique-character-in-a-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/first-unique-character-in-a-string/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def firstUniqChar(self, s):
            """
            :type s: str
            :rtype: int
            """
            NO_UNIQ = -1
            ch_dict = {}
            for i in range(0, len(s)):
                ch = s[i]
                if ch_dict.has_key(ch) is True:
                    ch_dict[ch] = NO_UNIQ
                else:
                    ch_dict[ch] = i
    
            if len(ch_dict.keys()) == 0:
                return -1
    
            min_index = -1
            for ch in ch_dict:
                if ch_dict[ch] == NO_UNIQ:
                    continue
                if min_index == -1:
                    min_index = ch_dict[ch]
                else:
                    if ch_dict[ch] < min_index:
                        min_index = ch_dict[ch]
            return min_index