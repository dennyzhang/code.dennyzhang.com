# Leetcode: Keyboard Row     :BLOG:Basic:


---

Check string are in one row of American keyboard  

---

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.  

    Example 1:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

Note:  
-   You may use one character in the keyboard more than once.
-   You may assume the input string will only contain letters of alphabet.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/keyboard-row)  

Credits To: [Leetcode.com](https://leetcode.com/problems/keyboard-row/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def findWords(self, words):
            """
            :type words: List[str]
            :rtype: List[str]
            """
            return_list = 
            character_dict = {}
            for ch in "qwertyuiop":
                character_dict[ch] = 0
            for ch in "asdfghjkl":
                character_dict[ch] = 1
            for ch in "zxcvbnm":
                character_dict[ch] = 2
    
            for word in words:
                lower_word = word.lower()
                is_ok = True
                index_key = -1
                for ch in lower_word:
                    if character_dict.has_key(ch) is False:
                        raise Exception("Unexpected character(%s) in %s" % (ch, word))
                    if index_key == -1:
                        index_key = character_dict[ch]
                    else:
                        if index_key != character_dict[ch]:
                            is_ok = False
                            break
                if is_ok is True:
                    return_list.append(word)
            return return_list