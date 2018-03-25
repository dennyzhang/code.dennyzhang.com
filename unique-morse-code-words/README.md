# Leetcode: Unique Morse Code Words     :BLOG:Basic:


---

Unique Morse Code Words  

---

Similar Problems:  
-   Tag: [#hashmap](https://brain.dennyzhang.com/tag/hashmap), [#string](https://brain.dennyzhang.com/tag/string)

---

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-&#x2026;", "c" maps to "-.-.", and so on.  

For convenience, the full table for the 26 letters of the English alphabet is given below:  

    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-&#x2026;.-", (which is the concatenation "-.-." + "-&#x2026;" + ".-"). We'll call such a concatenation, the transformation of a word.  

Return the number of different transformations among all words we have.  

Example:  

    Input: words = ["gin", "zen", "gig", "msg"]
    Output: 2
    Explanation: 
    The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."

There are 2 different transformations, "&#x2013;&#x2026;-." and "&#x2013;&#x2026;&#x2013;.".  

Note:  

-   The length of words will be at most 100.
-   Each words[i] will have length in range [1, 12].
-   words[i] will only consist of lowercase letters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/unique-morse-code-words)  

Credits To: [leetcode.com](https://leetcode.com/problems/unique-morse-code-words/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/unique-morse-code-words
    ## Basic Ideas: Hashmap
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def uniqueMorseRepresentations(self, words):
            """
            :type words: List[str]
            :rtype: int
            """
            l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            morseWords = set([])
            for word in words:
                item = ''
                for ch in word:
                    item += l[ord(ch)-ord('a')]
                morseWords.add(item)
            return len(morseWords)