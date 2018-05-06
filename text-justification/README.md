# Leetcode: Text Justification     :BLOG:Hard:


---

Text Justification  

---

Similar Problems:  
-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.  

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.  

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.  

For the last line of text, it should be left justified and no extra space is inserted between words.  

For example,  

    words: ["This", "is", "an", "example", "of", "text", "justification."]
    L: 16.

Return the formatted lines as:  

    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]

Note: Each word is guaranteed not to exceed L in length.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/text-justification)  

Credits To: [leetcode.com](https://leetcode.com/problems/text-justification/description/)  

Leave me comments, if you have better ways to solve.  

    func fullJustify(words []string, maxWidth int) []string {
    
    }